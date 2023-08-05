import traceback
import telegram
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from config import notification_channel, authorized_users, chatbot_token
from db import insert_event, set_confirmed, get_event_from_id
from event import category2emoji, Event, check_events_collision, BadEventAttrError
from notification import check_event_will_get_published, publish_event


(LOCANDINA, DATA_INIZIO, DATA_FINE, DATA_FINE_2, 
 ORARIO_INIZIO, ORARIO_FINE, ORARIO_FINE_2, 
 LOCATION, TITOLO, CATEGORIA, DESCRIZIONE, CONFERMA, ROUTE_SAME_EVENT) = range(13)
TOKEN = chatbot_token

def evento(update, context) -> int:
    """Starts adding an event asking for picture of event"""
    update.message.reply_text(
        "Bene! Per iniziare invia la locandina dell'evento. "
        "Invia /cancel in qualsiasi momento per interrompere la conversazione.")
    context.user_data['event'] = Event()
    return LOCANDINA


def locandina(update, context) -> int:
    """Stores the photo and asks for a date."""
    photo_file = update.message.photo[-1].file_id
    context.user_data['locandina'] = photo_file
    update.message.reply_text("Come si chiama l'evento?")
    return TITOLO


def titolo(update, context) -> int:
    """Asks for description of event"""
    try:
        context.user_data['event'].name = update.message.text
        update.message.reply_text("Ora inserisci il luogo dell'evento: [ad esempio: Teatro Petruzzelli, Bari]")
        return LOCATION
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return TITOLO


def location(update, context) -> int:
    """Asks for title of event"""
    try:
        context.user_data['event'].venue = update.message.text
        update.message.reply_text("Perfetto! Ora inserisci la data di inizio evento: [formato gg.mm.aaaa]")
        return DATA_INIZIO
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return LOCATION
    

def data_inizio(update, context) -> int:
    """Stores date and asks if ending date."""
    try:
        context.user_data['event'].start_date = update.message.text
        update.message.reply_text("A che ora inizia l'evento? [formato hh:mm]")
        return ORARIO_INIZIO
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return DATA_INIZIO


def orario_inizio(update, context) -> int:
    """Stores Asks if end time"""
    try:
        context.user_data['event'].start_time = update.message.text
        colliding_event = check_events_collision(context.user_data['event'])
        if colliding_event is not None:
            update.message.reply_text("Un evento simile al tuo è già stato proposto:")
            update.message.reply_text(colliding_event.html(), parse_mode=telegram.ParseMode.HTML)
            update.message.reply_text("Si tratta dello stesso evento?", 
            reply_markup=ReplyKeyboardMarkup([["Sì", "No"]], one_time_keyboard=True, input_field_placeholder="Sì o no?"))
            return ROUTE_SAME_EVENT
        else:
            update.message.reply_text("Ok! L'evento ha una data di fine diversa da quella di inizio?", 
                reply_markup=ReplyKeyboardMarkup([["Sì", "No"]], one_time_keyboard=True, input_field_placeholder="Sì o no?"))
            return DATA_FINE
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return ORARIO_INIZIO


def route_same_event(update, context) -> int:
    """Routes conversation based on whether the event is the same."""
    user_input = update.message.text.strip().lower()
    if user_input == 'sì':
        update.message.reply_text("Ok allora, grazie lo stesso!")
        return ConversationHandler.END
    elif user_input == 'no':
        update.message.reply_text("Ok! L'evento ha una data di fine diversa da quella di inizio?", 
        reply_markup=ReplyKeyboardMarkup([["Sì", "No"]], one_time_keyboard=True, input_field_placeholder="Sì o no?"))
        return DATA_FINE


def data_fine(update, context) -> int:
    """Asks for ending date."""
    update.message.reply_text("Inserisci la data di fine evento: [formato gg.mm.aaaa]")
    return DATA_FINE_2


def data_fine_2(update, context) -> int:
    """Stores ending date, asks for time"""
    try:
        context.user_data['event'].end_date = update.message.text
        update.message.reply_text("A che ora finisce l'evento? [formato hh:mm]")
        return ORARIO_FINE_2
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return DATA_FINE_2


def skip_data_fine(update, context) -> int:
    update.message.reply_text("Vuoi inserire l'orario di fine evento?", 
        reply_markup=ReplyKeyboardMarkup([["Sì", "No"]], one_time_keyboard=True, input_field_placeholder="Sì o no?"))
    return ORARIO_FINE


def orario_fine(update, content) -> int:
    """Asks end time"""
    update.message.reply_text("A che ora finisce l'evento? [formato hh:mm]")
    return ORARIO_FINE_2
    

def orario_fine_2(update, context) -> int:
    """stores end time and asks location"""
    try:
        context.user_data['event'].end_time = update.message.text
        update.message.reply_text("Scegli una categoria per l'evento:",
        reply_markup=ReplyKeyboardMarkup([[emoji + " " + category] for category, emoji in category2emoji.items()],
            one_time_keyboard=True, input_field_placeholder="Scegli una categoria..."))
        return CATEGORIA
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return ORARIO_FINE_2


def skip_orario_fine(update, context) -> int:
    """Skips end time asks for location"""
    update.message.reply_text("Scegli una categoria per l'evento:",
    reply_markup=ReplyKeyboardMarkup([[emoji + " " + category] for category, emoji in category2emoji.items()],
        one_time_keyboard=True, input_field_placeholder="Scegli una categoria..."))
    return CATEGORIA


def categoria(update, context) -> int:
    """Choose one or more category for the event."""
    category = update.message.text[2:]
    if category not in category2emoji:
        update.message.reply_text("La categoria che hai scelto non è tra quelle previste. Usa la tastiera preimpostata:",
            reply_markup=ReplyKeyboardMarkup([[emoji + " " + category] for category, emoji in category2emoji.items()],
                one_time_keyboard=True, input_field_placeholder="Scegli una categoria..."))
        return CATEGORIA
    context.user_data['event'].categories = category
    update.message.reply_text("Inserisci le info utili per l'evento (come link per acquistare biglietti, programmi, line-up, etc):")
    return DESCRIZIONE


def descrizione(update, context) -> int:
    try:
        context.user_data['event'].description = update.message.text
    except BadEventAttrError as e:
        update.message.reply_text(str(e))
        return DESCRIZIONE
    try:
        username = update.message.from_user.username
        primonome = update.message.from_user.first_name
        update.message.reply_photo(
            photo=context.user_data['locandina'],
            caption=context.user_data['event'].html(),
            parse_mode=telegram.ParseMode.HTML)
        update.message.reply_text("Sei sicur* di voler consigliare quest'evento?", reply_markup=ReplyKeyboardMarkup(
            [["Sì", "No"]], one_time_keyboard=True, input_field_placeholder="Sì o no?"))
        return CONFERMA
    except telegram.error.BadRequest:
        update.message.reply_text("Si è verificato un errore con la generazione del messaggio :( \n Prova a cambiare leggermente la descrizione o il titolo o contatta i creatori del bot @luigijs e @shift97 per assistenza")
        telegram.Bot(token=TOKEN).sendMessage(chat_id=notification_channel,text=f"{primonome}, @{username} ha provato ad inviare un evento ma si è verificato un errore")
        print(traceback.format_exc())
        return ConversationHandler.END


def conferma(update, context) -> int:
    """sends the event to notification_channel"""
    username = update.message.from_user.username
    primonome = update.message.from_user.first_name
    user_id = update.message.from_user.id
    event = context.user_data['event']

    if user_id in authorized_users:
        event.confirmed = True
        telegram.Bot(token=TOKEN).send_photo(
                chat_id=notification_channel,
                photo=context.user_data['locandina'],
                caption=event.html(),
                parse_mode=telegram.ParseMode.HTML
            )
        telegram.Bot(token=TOKEN).sendMessage(chat_id=notification_channel, text=f"Inviato da {primonome}, @{username}.")
        update.message.reply_text("L'evento è stato programmato per la pubblicazione. Grazie!")
        event_id = insert_event(event)
        update.message.reply_text(f"Questo è il codice unico del tuo evento: <code>{event.hash()}</code>. "
            "Puoi usarlo con il comando /modifica per cambiare alcune informazioni sull'evento prima della pubblicazione.",
            parse_mode=telegram.ParseMode.HTML)
        if check_event_will_get_published(event) == False:
            publish_event(telegram.Bot(token=TOKEN), event)
    else:
        telegram.Bot(token=TOKEN).send_photo(
                chat_id=notification_channel,
                photo=context.user_data['locandina'],
                caption=event.html(),
                parse_mode=telegram.ParseMode.HTML
            )
        event_id = insert_event(event)
        telegram.Bot(token=TOKEN).sendMessage(chat_id=notification_channel, text=f"Inviato da {primonome}, @{username}.")
        telegram.Bot(token=TOKEN).sendMessage(chat_id=notification_channel, text="Confermare?",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text='Sì', callback_data=f"{user_id} {event_id} 1"),
                                                InlineKeyboardButton(text='No', callback_data=f"{user_id} {event_id} 0")]]))
        update.message.reply_text("L'evento è stato inviato ai moderatori. Grazie per la richiesta!")

    file_locandina = telegram.Bot(token=TOKEN).get_file(context.user_data['locandina'])
    file_locandina.download(f'locandine/{event_id}.jpg')
    return ConversationHandler.END


def cancel(update, context) -> int:
    """Cancels and ends the conversation."""
    update.message.reply_text("Ok, operazione annullata.")
    return ConversationHandler.END


event_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("evento", evento)],
        states={
            LOCANDINA: [MessageHandler(filters.Filters.photo, locandina)],
            DATA_INIZIO: [MessageHandler(filters.Filters.text, data_inizio)],
            DATA_FINE: [MessageHandler(filters.Filters.regex("Sì"), data_fine),
                MessageHandler(filters.Filters.regex("No"), skip_data_fine)],
            DATA_FINE_2: [MessageHandler(filters.Filters.text, data_fine_2)],
            ORARIO_INIZIO: [MessageHandler(filters.Filters.text, orario_inizio)],
            ROUTE_SAME_EVENT: [MessageHandler(filters.Filters.text, route_same_event)],
            ORARIO_FINE: [MessageHandler(filters.Filters.regex("Sì"), orario_fine),
                MessageHandler(filters.Filters.regex("No"), skip_orario_fine)],
            ORARIO_FINE_2: [MessageHandler(filters.Filters.text, orario_fine_2)],
            LOCATION: [MessageHandler(filters.Filters.text & (~ filters.Filters.command), location)],
            TITOLO: [MessageHandler(filters.Filters.text & (~ filters.Filters.command), titolo)],
            CATEGORIA: [MessageHandler(filters.Filters.text & (~ filters.Filters.command), categoria)],
            DESCRIZIONE: [MessageHandler(filters.Filters.text & (~ filters.Filters.command), descrizione)],
            CONFERMA: [MessageHandler(filters.Filters.regex("Sì"), conferma),
                MessageHandler(filters.Filters.regex("No"), cancel)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )


def set_event_confirmation(update, context) -> None:
    """Called in response to pressing of InlineKeyboardButton. Either confirms or
    does not confirm an event."""
    callback_data = update.callback_query.data
    admin = update.callback_query.from_user
    user_id = int(callback_data.split()[0])
    event_id = int(callback_data.split()[1])
    confirmed = bool(int(callback_data.split()[2]))

    if confirmed:
        set_confirmed(event_id)
        event = Event().load_from_res(get_event_from_id(event_id)[0])
        update.callback_query.edit_message_text(text=f"Evento confermato da {admin.first_name}, @{admin.username}.")
        telegram.Bot(token=TOKEN).sendMessage(chat_id=user_id, text=f"L'evento che hai proposto è stato accettato e programmato per la pubblicazione. Grazie!")
        telegram.Bot(token=TOKEN).sendMessage(chat_id=user_id, text=f"Questo è il codice unico del tuo evento: <code>{event.hash()}</code>. "
            "Puoi usarlo con il comando /modifica per cambiare alcune informazioni sull'evento prima della pubblicazione.",
            parse_mode=telegram.ParseMode.HTML)
        if check_event_will_get_published(event) == False:
            publish_event(telegram.Bot(token=TOKEN), event)
    else:
        update.callback_query.edit_message_text(text=f"Evento non confermato da {admin.first_name}, @{admin.username}.")
        telegram.Bot(token=TOKEN).sendMessage(chat_id=user_id,
            text=f"Ti ringraziamo per la tua proposta, ma abbiamo deciso di non condividere l'evento che hai suggerito. \
                   Probabilmente non è il tipo di evento che ci proponiamo di promuovere, \
                   puoi leggere di più a riguardo qui: www.apuliacore.org/manifesto.html. \
                   Se vuoi parlare con noi, puoi scriverci nel gruppo Telegram o sulla nostra pagina Instagram.")


callback_query_handler = CallbackQueryHandler(set_event_confirmation)
