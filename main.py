import discord
from discord.ext import commands
import os

TOKEN = os.getenv("TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))
VERIFICATION_CHANNEL_ID = int(os.getenv("VERIFICATION_CHANNEL_ID"))
MOD_LOG_CHANNEL_ID = int(os.getenv("MOD_LOG_CHANNEL_ID"))
VERIFIED_ROLE_ID = int(os.getenv("VERIFIED_ROLE_ID"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

class VerifyView(discord.ui.View):
    def __init__(self, user: discord.Member):
        super().__init__(timeout=None)
        self.user = user

    @discord.ui.button(label="✅ Approve", style=discord.ButtonStyle.success)
    async def approve(self, interaction: discord.Interaction, button: discord.ui.Button):
        role = interaction.guild.get_role(VERIFIED_ROLE_ID)
        await self.user.add_roles(role)
        await interaction.response.send_message(f"{self.user.mention} has been verified!", ephemeral=False)

    @discord.ui.button(label="❌ Deny", style=discord.ButtonStyle.danger)
    async def deny(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f"{self.user.mention} has been denied.", ephemeral=False)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.channel.id != VERIFICATION_CHANNEL_ID or message.author.bot:
        return

    if message.attachments:
        mod_log_channel = bot.get_channel(MOD_LOG_CHANNEL_ID)
        await mod_log_channel.send(
            content=f"📸 New verification from {message.author.mention}",
            files=[await att.to_file() for att in message.attachments],
            view=VerifyView(message.author)
        )

bot.run(TOKEN)
