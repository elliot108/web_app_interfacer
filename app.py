from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from bot_credentials import BOT_TOKEN, BOT_USERNAME
import json

async def launch_web_ui(update: Update, callback: CallbackContext):
    # For now, let's just acknowledge that we received the command
    kb = [
        [
            KeyboardButton("Show me my web app", web_app= WebAppInfo("https://jihulab.com/elliot108/web_app_interfacer/"))
        ]
    ]
    await update.effective_chat.send_message("Let's do it", reply_markup=ReplyKeyboardMarkup(kb))

print(BOT_TOKEN)

async def web_app_data(update: Update, context: CallbackContext):
    data = json.loads(update.message.web_app_data.data)
    await update.message.reply_text("Your data was:")
    for result in data:
        await update.message.reply_text(f"{result['name']}: {result['value']}")



if __name__ == '__main__':
    # when we run the script we want to first create the bot from the token:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # and let's set a command listener for /start to trigger our Web UI
    application.add_handler(CommandHandler('start', launch_web_ui))

    # as well as a web-app listener for the user-inputted data
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))


    # and send the bot on its way!
    print(f"Your bot is listening! Navigate to http://t.me/{BOT_USERNAME} to interact with it!")
    application.run_polling()
