import telegram
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import openai
import logging

# Thiết lập API key trực tiếp
openai.api_key = "sk-proj-srgEktqpi5wjH7wm7us3T3BlbkFJqrDljTieTjySitISAq5Q"

# Thay thế bằng token và API key của bạn
TELEGRAM_BOT_TOKEN = '7298636923:AAGL9e1cIJ1rVcjZ7BAkcpoBleAs7JGPhJs'
OPENAI_API_KEY = 'sk-proj-srgEktqpi5wjH7wm7us3T3BlbkFJqrDljTieTjySitISAq5Q'

# Cấu hình logging để ghi lại các lỗi
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Chào mừng bạn đến với ChatGPT Bot!')

async def chatgpt(update: telegram.Update, context: telegram.ext.ContextTypes.DEFAULT_TYPE):
    try:
        user_message = update.message.text
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )
        bot_response = completion.choices[0].message.content
        await update.message.reply_text(bot_response)
    except Exception as e:
        logger.error(f"Error in chatgpt function: {e}")
        await update.message.reply_text("Đã xảy ra lỗi. Vui lòng thử lại sau.")

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Thêm các handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chatgpt))

    # Error handler để ghi lại các lỗi
    application.add_error_handler(lambda update, context: logger.error(f"Update {update} caused error {context.error}"))

    # Chạy bot
    application.run_polling()

if __name__ == '__main__':
    main()

