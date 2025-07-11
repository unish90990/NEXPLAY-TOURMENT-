# 📸 Discord Screenshot Verification Bot

A Python Discord bot to handle screenshot-based verification using moderator approval buttons.

---

## ✅ Features

- Users upload screenshots in a public channel
- Moderators receive the screenshot with Approve/Deny buttons
- Verified users receive a role

---

## 🛠 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/discord-verification-bot.git
   cd discord-verification-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add a `.env` file with:
   ```
   TOKEN=your_bot_token
   GUILD_ID=your_guild_id
   VERIFICATION_CHANNEL_ID=your_verification_channel_id
   MOD_LOG_CHANNEL_ID=your_mod_review_channel_id
   VERIFIED_ROLE_ID=your_verified_role_id
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

---

## ☁️ Deploying to Railway

1. Go to [https://railway.app](https://railway.app)
2. Create a New Project → Deploy from GitHub
3. Link this repo
4. Add Environment Variables as shown above
5. Deploy and you’re live 🚀

---

Made with ❤️ by you + ChatGPT
