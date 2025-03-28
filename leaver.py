from telethon import TelegramClient
from datetime import datetime, timedelta
import asyncio
from telethon.errors import FloodWaitError
from telethon.errors import SessionPasswordNeededError

# Funzione per l'autenticazione 2FA
async def login_with_2fa(client):
    try:
        # Tentativo di accesso
        await client.start()
    except SessionPasswordNeededError:
        # Se è richiesta la password per la 2FA
        password = input("Inserisci il codice di autenticazione 2FA: ")
        await client.start(password=password)

# Funzione per controllare l'input numerico
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Per favore inserisci un numero positivo.")
        except ValueError:
            print("Valore non valido. Inserisci un numero intero positivo.")

# Arte ASCII di benvenuto con "TUCL"
def print_welcome_message():
    welcome_message = """
    ████████████   ██   ███████╗████████╗███████╗
    ██╔══════██╗  ██   ██╔════╝╚══██╔══╝██╔════╝
    █████╗  ███████╗██   █████╗     ██║   █████╗  
    ██╔══╝  ██╔══██╗██   ██╔══╝     ██║   ██╔══╝  
    ███████╗██║  ██║██   ███████╗   ██║   ███████╗
    ╚══════╝╚═╝  ╚═╝╚═╝ ╚══════╝   ╚═╝   ╚══════╝
    """
    print(welcome_message)

# Chiedi all'utente le informazioni per il login
api_id = input("Inserisci il tuo API ID: ")
api_hash = input("Inserisci il tuo API Hash: ")

# Configurazioni
INACTIVE_DAYS = get_positive_integer("Inserisci il numero di giorni di inattività per considerare una chat abbandonata (es. 30): ")
WHITELIST = []

# Impostiamo il client di Telegram
client = TelegramClient('session_name', api_id, api_hash)

async def leave_old_chats():
    print("Benvenuto in Telegram Unused Chat Leaver!")
    
    await login_with_2fa(client)

    # Ottieni tutte le chat (dialoghi)
    dialogs = await client.get_dialogs()

    # Calcola la soglia di inattività
    inactive_time_threshold = timedelta(days=INACTIVE_DAYS)

    abandoned_chats = {'personal': 0, 'group': 0, 'channel': 0}

    # Loop attraverso ogni chat (dialogo)
    for dialog in dialogs:
        # Salta le chat nella whitelist
        if dialog.id in WHITELIST:
            print(f"Saltata la chat in whitelist: {dialog.name}")
            continue
        
        # Ottieni il timestamp dell'ultimo messaggio della chat
        last_message = dialog.message
        if last_message and isinstance(last_message.date, datetime):
            last_message_time = last_message.date
        else:
            continue  # Salta se non c'è un messaggio valido o una data

        # Rendi entrambe le date naive (senza informazioni sul fuso orario)
        now = datetime.now()
        last_message_time_naive = last_message_time.replace(tzinfo=None)

        # Se la chat è inattiva e il tipo corrisponde alla selezione
        if now - last_message_time_naive > inactive_time_threshold:
            # Incrementa il contatore per il tipo di chat
            if dialog.is_group:
                abandoned_chats['group'] += 1
            elif dialog.is_channel:
                abandoned_chats['channel'] += 1
            else:
                abandoned_chats['personal'] += 1
            
            print(f"Lasciando la chat: {dialog.name} (Ultimo messaggio: {last_message_time_naive})")
            try:
                await client.delete_dialog(dialog.id)  # Rimuove la chat dalla tua lista
            except FloodWaitError as e:
                print(f"Limite raggiunto, aspetterò {e.seconds} secondi prima di continuare...")
                await asyncio.sleep(e.seconds)
                continue

    print(f"Fatto! Ho lasciato {abandoned_chats['personal']} chat personali, {abandoned_chats['group']} chat di gruppo e {abandoned_chats['channel']} canali.")
    print(f"Chat abbandonate totali: {abandoned_chats['personal'] + abandoned_chats['group'] + abandoned_chats['channel']}")

# Funzione principale
def main():
    print_welcome_message()
    
    print("Telegram Unused Chat Leaver - Gestione chat abbandonate")
    
    # Offri l'opzione di inserire una whitelist
    add_to_whitelist = input("Vuoi aggiungere delle chat alla whitelist? (y/n): ")
    if add_to_whitelist.lower() == 'y':
        print("Aggiungi gli ID delle chat da non abbandonare:")
        while True:
            chat_id = input("Inserisci l'ID della chat da aggiungere alla whitelist (oppure digita 'fine' per terminare): ")
            if chat_id.lower() == 'fine':
                break
            else:
                try:
                    WHITELIST.append(int(chat_id))
                except ValueError:
                    print("ID chat non valido. Inserisci un numero intero.")

    # Selezione tipo di chat da abbandonare
    print("\nScegli il tipo di chat da abbandonare:")
    print("1. Chat Personali")
    print("2. Gruppi")
    print("3. Canali")
    chat_type_choice = input("Inserisci il numero corrispondente alla tua scelta (1/2/3): ")

    if chat_type_choice == '1':
        print("Abbandonerò solo le chat personali.")
    elif chat_type_choice == '2':
        print("Abbandonerò solo i gruppi.")
    elif chat_type_choice == '3':
        print("Abbandonerò solo i canali.")
    else:
        print("Scelta non valida. Verranno abbandonate tutte le chat.")
    
    # Esegui la funzione per lasciare le chat vecchie
    client.loop.run_until_complete(leave_old_chats())

if __name__ == "__main__":
    main()
