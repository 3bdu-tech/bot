
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from smart_bot_fully_contextual_final_ready_with_my_courses_updated import (
    TOKEN, start, start_course_registration, handle_user,
    show_my_lectures, show_my_exams, my_info, show_lectures, show_exams
)

app = Flask(__name__)
bot_app = ApplicationBuilder().token(TOKEN).build()

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(CommandHandler("register", start_course_registration))
bot_app.add_handler(CommandHandler("l", show_my_lectures))
bot_app.add_handler(CommandHandler("e", show_my_exams))
bot_app.add_handler(CommandHandler("in", my_info))
bot_app.add_handler(CommandHandler("viewl", show_lectures))
bot_app.add_handler(CommandHandler("viewe", show_exams))
bot_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_user))

@app.route(f"/webhook/{{TOKEN}}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    await bot_app.process_update(update)
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
