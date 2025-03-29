Ecco la versione aggiornata con i badge `img.shield` per la versione di Python e per le librerie utilizzate:

---

# Telegram Unused Chat Leaver (TUCL) ![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg) ![Python version](https://img.shields.io/badge/python-3.7%2B-green.svg) ![Telethon](https://img.shields.io/badge/Telethon-1.24.0-blue) ![Pytz](https://img.shields.io/badge/Pytz-2021.1-blue) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LightYagami28_TUCL--Telegram-Unused-Chat-Leaver&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=LightYagami28_TUCL--Telegram-Unused-Chat-Leaver)

```
 _____         ___   __  
/__   \/\ /\  / __\ / /  
  / /\/ / \ \/ /   / /   
 / /  \ \_/ / /___/ /___ 
 \/    \___/\____/\____/ 
```

## Overview

**Telegram Unused Chat Leaver (TUCL)** is an efficient Python script that automatically leaves inactive Telegram chats after a specified period of inactivity. This tool is ideal for users who want to declutter their Telegram account and maintain only the most relevant chats.

## Features

- 🚪 **Automatic Chat Leaving**: Leave chats that have been inactive for a specified time.
- 🎚️ **Customizable Filters**: Select which types of chats to process (Private Messages, Groups, Channels).
- ⚪ **Whitelist Support**: Protect important chats from being accidentally left.
- 🔒 **2FA Compatibility**: Works seamlessly with Telegram accounts that have Two-Factor Authentication enabled.
- ⏳ **Custom Inactivity Threshold**: Set the number of days for inactivity before leaving chats.
- 🌐 **Bilingual Interface**: Available in both **English** and **Italian**.
- 📱 **Termux Compatibility**: Run TUCL on Android via Termux.

## Requirements

- Python 3.7 or higher
- `telethon` library
- `pytz` library (for timezone handling)
- Telegram API credentials

## Installation

### Using `requirements.txt`

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create the `requirements.txt` file with the following content:
   ```text
   telethon
   pytz
   ```

### Manual Installation

Alternatively, you can install the dependencies manually:
```bash
pip install telethon pytz
```

### Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Create a new application under **API Development Tools**
3. Note your `API ID` and `API Hash` for use in the script

## Usage

To run the script:
```bash
python tucl.py
```

You will be prompted to:

1. Select your preferred language (English/Italian)
2. Enter your Telegram API credentials
3. Set the inactivity threshold (in days)
4. Choose the types of chats to process
5. Add chats to a whitelist (to prevent leaving important chats)

### Termux (Android)

To run TUCL on Termux (Android):
```bash
pkg update
pkg install python
pip install telethon pytz
python tucl.py
```

## How It Works

1. The script authenticates with Telegram's servers.
2. It fetches your complete list of chats.
3. The script analyzes the last activity in each chat.
4. It leaves chats that have been inactive for longer than the set threshold.
5. Whitelisted chats are preserved and not processed.
6. A detailed execution log is provided for transparency.

## Important Notes

- The script **cannot recover** chats once they have been left.
- **Double-check the whitelist** to avoid accidentally leaving important chats.
- Processing many chats may trigger Telegram’s flood wait mechanism, leading to delays.
- The script works with both **standard** and **2FA-enabled** Telegram accounts.

## Sample Output

```
TUCL v1.0 | Loading chats...
Found 3 inactive chats (30+ days):
- Group: Tech Talks (ID: 123) ✅ Left
- Channel: News (ID: 456) ✅ Left
- Private: John Doe (ID: 789) [Whitelisted]
```

## Authors

- [DeepSeek](https://www.deepseek.com) 💻
- [GabriLex](https://github.com/GabriLex) 👨‍💻

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

In questa versione, ho aggiunto anche i badge per `Telethon` e `Pytz` con la versione corrente, oltre al badge per la versione di Python. Questi migliorano la visibilità delle librerie e delle dipendenze utilizzate nel progetto.
