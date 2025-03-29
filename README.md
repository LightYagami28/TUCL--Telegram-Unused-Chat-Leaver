# Telegram Unused Chat Leaver (TUCL)

```
 _____         ___   __  
/__   \/\ /\  / __\ / /  
  / /\/ / \ \/ /   / /   
 / /  \ \_/ / /___/ /___ 
 \/    \___/\____/\____/ 
```

## Overview

**Telegram Unused Chat Leaver (TUCL)** is a Python script designed to automatically leave inactive Telegram chats after a specified period of inactivity.

## Features
- 🚪 Automatically leaves inactive chats
- 🎚️ Customizable chat type selection (Private Messages, Groups, Channels)
- ⚪ Whitelist support to preserve important chats
- 🔒 Fully compatible with Two-Factor Authentication (2FA)
- ⏳ Configurable inactivity threshold (in days)
- 🌐 Bilingual interface (English/Italian)
- 📱 Compatible with Termux (Android)

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
2. Create a new application under "API Development Tools"
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
6. A detailed execution log is provided.

## Important Notes
- The script **cannot recover** chats once they have been left.
- Double-check the whitelist to avoid accidentally leaving important chats.
- Processing many chats may trigger Telegram’s flood wait mechanism.
- The script works with both standard and 2FA-enabled Telegram accounts.

## Sample Output
```
TUCL v1.0 | Loading chats...
Found 3 inactive chats (30+ days):
- Group: Tech Talks (ID: 123) ✅ Left
- Channel: News (ID: 456) ✅ Left
- Private: John Doe (ID: 789) [Whitelisted]
```

## Authors
- [DeepSeek](https://www.deepseek.com)
- [GabriLex](https://github.com/GabriLex)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
