from telethon import TelegramClient
from telethon.errors import FloodWaitError
from telethon.tl.types import PeerChat, PeerUser, PeerChannel
from datetime import datetime, timedelta
import pytz

# ASCII Art
ASCII_ART = r'''
 _____         ___   __  
/__   \/\ /\  / __\ / /  
  / /\/ / \ \/ /   / /   
 / /  \ \_/ / /___/ /___ 
 \/    \___/\____/\____/ 
'''

print(ASCII_ART)

# Language selection
def get_language():
    print("Select language / Scegli lingua:")
    print("1. English")
    print("2. Italiano")
    choice = input("Enter choice / Inserisci scelta (1-2): ")
    return 'en' if choice == '1' else 'it'

language = get_language()

# Translations
translations = {
    'welcome': {
        'en': "Welcome to Telegram Unused Chat Leaver!",
        'it': "Benvenuto in Telegram Unused Chat Leaver!"
    },
    'api_id': {
        'en': "Enter your API ID: ",
        'it': "Inserisci il tuo API ID: "
    },
    'api_hash': {
        'en': "Enter your API Hash: ",
        'it': "Inserisci il tuo API Hash: "
    },
    'inactive_days': {
        'en': "Enter the number of days for inactivity threshold: ",
        'it': "Inserisci il numero di giorni per la soglia di inattività: "
    },
    'chat_type': {
        'en': "\nSelect the type of chats you want to leave:",
        'it': "\nSeleziona il tipo di chat che vuoi abbandonare:"
    },
    'chat_options': {
        'en': ["1. Personal chats", "2. Groups", "3. Channels", "4. All"],
        'it': ["1. Chat personali", "2. Gruppi", "3. Canali", "4. Tutti"]
    },
    'filtered_chats': {
        'en': "\nFiltered Chats List (ID, Name, Type):",
        'it': "\nLista Chat Filtate (ID, Nome, Tipo):"
    },
    'whitelist_prompt': {
        'en': "\nEnter chat IDs to whitelist (comma separated, or Enter to skip):",
        'it': "\nInserisci gli ID delle chat da escludere (separati da virgola, o Invio per saltare):"
    },
    'checking': {
        'en': "\nChecking for inactive chats...",
        'it': "\nControllo delle chat inattive in corso..."
    },
    'left_chat': {
        'en': "Left {} (ID: {})",
        'it': "Abbandonato {} (ID: {})"
    },
    'flood_wait': {
        'en': "Flood wait error. Try again in {} seconds.",
        'it': "Errore flood wait. Riprova tra {} secondi."
    },
    'error_leaving': {
        'en': "Error leaving chat {} (ID: {}): {}",
        'it': "Errore nell'abbandonare la chat {} (ID: {}): {}"
    },
    'whitelisted': {
        'en': "Skipping whitelisted chat {} (ID: {})",
        'it': "Salto la chat in whitelist {} (ID: {})"
    },
    'still_active': {
        'en': "{} (ID: {}) is still active.",
        'it': "{} (ID: {}) è ancora attiva."
    },
    'no_messages': {
        'en': "{} (ID: {}) has no messages.",
        'it': "{} (ID: {}) non ha messaggi."
    }
}

def t(key):
    return translations[key][language]

print(t('welcome'))

# Telegram API configuration
api_id = input(t('api_id'))
api_hash = input(t('api_hash'))

# Inactivity settings
inactive_days = int(input(t('inactive_days')))
inactive_time_threshold = timedelta(days=inactive_days)

async def main():
    # Create Telethon client inside async function
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()

    # Whitelist
    whitelist = set()

    dialogs = await client.get_dialogs()

    # Select chat type to leave
    print(t('chat_type'))
    for option in t('chat_options'):
        print(option)
    choice = input()

    filtered_dialogs = []

    # Filter by chat type and show immediately
    print("\n" + t('filtered_chats'))
    for dialog in dialogs:
        if choice == '1' and isinstance(dialog.entity, PeerUser):
            print(f"ID: {dialog.id}, Name: {dialog.name}, Type: Personal Chat")
            filtered_dialogs.append(dialog)
        elif choice == '2' and isinstance(dialog.entity, PeerChat):
            print(f"ID: {dialog.id}, Name: {dialog.name}, Type: Group")
            filtered_dialogs.append(dialog)
        elif choice == '3' and isinstance(dialog.entity, PeerChannel):
            print(f"ID: {dialog.id}, Name: {dialog.name}, Type: Channel")
            filtered_dialogs.append(dialog)
        elif choice == '4':
            print(f"ID: {dialog.id}, Name: {dialog.name}, Type: Any")
            filtered_dialogs.append(dialog)

    # Ask for whitelist after showing all chats
    print("\n" + t('whitelist_prompt'))
    whitelist_input = input().strip()
    if whitelist_input:
        whitelist.update(map(int, whitelist_input.split(',')))

    print(t('checking'))
    now = datetime.now(pytz.utc)

    for dialog in filtered_dialogs:
        last_message = dialog.message
        if last_message:
            last_message_time = last_message.date
            if last_message_time.tzinfo is None:
                last_message_time = last_message_time.replace(tzinfo=pytz.utc)
            
            if now - last_message_time > inactive_time_threshold:
                if dialog.id not in whitelist:
                    try:
                        await client.delete_dialog(dialog.id)
                        print(t('left_chat').format(dialog.name, dialog.id))
                    except FloodWaitError as e:
                        print(t('flood_wait').format(e.seconds))
                    except Exception as e:
                        print(t('error_leaving').format(dialog.name, dialog.id, e))
                else:
                    print(t('whitelisted').format(dialog.name, dialog.id))
            else:
                print(t('still_active').format(dialog.name, dialog.id))
        else:
            print(t('no_messages').format(dialog.name, dialog.id))

    await client.disconnect()

# Run the main function
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
