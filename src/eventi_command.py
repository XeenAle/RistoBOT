from src.lib.lib import *
from typing import Any

## Funzione di gestione del comando /eventi
# Mostra la locandina dei prossimi eventi in formato .jpg
async def eventi_command(update: Update, context: CallbackContext, bot: Any = None) -> None:
    # Implementa la logica per visualizzare il menu
    await update.message.reply_text("Ecco il nostri eventi settimanali:")
    image_path = os.path.join("src", "media", "SpecialNightsEvents.jpeg")
    # Invia la foto utilizzando il bot
    with open(image_path, 'rb') as photo_file:
        await context.bot.sendPhoto(update.effective_chat.id, photo=photo_file)