import telebot
import os
from flask import Flask, request, render_template_string
from g4f import Provider, models
from langchain.llms.base import LLM
from langchain_g4f import G4FLLM
from modes import modes
from langchain.prompts import (
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

chat_history=[]
# bot setup
bot_key = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(bot_key)

url =os.environ["URL"]
# Flask app setup
app = Flask(__name__)

# modes setup
mode_names = list(modes.keys())
current_mode = modes["System"]

# keyboard setup
keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
for mode_name in mode_names:
    button = telebot.types.InlineKeyboardButton(
        text=mode_name, callback_data=mode_name)
    keyboard.add(button)

# Set webhook
bot.remove_webhook()  # Remove any existing webhook
bot.set_webhook(url=url)

# Initialize LLM
llm: LLM = G4FLLM(
    model=models.gpt_35_turbo,
    provider=Provider.Aura,
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        update = telebot.types.Update.de_json(
            request.stream.read().decode('utf-8'))
        message = update.message
        parse_message(message)
        return 'ok', 200
    else:
        return render_template_string("Running Padriono Bot")

@bot.message_handler(func=lambda message: not message.text.startswith('/'))
def generate_message(message):
    chat_id = message.chat.id
    prompt = message.text
    reply = bot.send_message(chat_id, "Thinking...")

    # Generate the chat prompt using the new function
    response = generate_chat_prompt(current_mode, prompt, bot, chat_id, reply.message_id)

    # Check if the response is empty or evaluates to False
    if not response:
        # Send a message indicating technical difficulties
        bot.send_message(chat_id=chat_id, text="Sorry we are having technical difficulties. Try again later")
    else:
        # If the response is not empty, edit the message with the response
        bot.edit_message_text(chat_id=chat_id, message_id=reply.message_id, text=response)


def generate_chat_prompt(system_message, human_message, bot, chat_id, message_id):
    # Create the system message prompt
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)
    # Create the human message prompt
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)
    # Combine the prompts into a chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # Format the chat prompt and convert it to messages
    messages = chat_prompt.format_prompt().to_messages()
    
    # Append the human message and response to the chat history
    chat_history.append((human_message, str(chat_prompt.format_prompt())))
    
    # Limit chat history to the last 10 entries
    if len(chat_history) > 10:
        chat_history.pop(0)  # Remove the oldest entry
    
    # Generate the response from the chatbot
    response = llm(str(chat_prompt.format_prompt()))
    
    return response

# /start
@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Enter a prompt, wait for a response.')


def parse_message(message):
    if message.text.startswith('/'):
        start_command(message)     
    else:
        # Handle regular message
        generate_message(message)

if __name__ == "__main__":
    # Run the Flask app
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT',  5000)))
