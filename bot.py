import pandas as pd
import random
import ast
import telebot



data = pd.read_csv("newdataset.csv")

bot_token = 'telegram_token'
bot = telebot.TeleBot(bot_token)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text.lower()
    tag_matches = data[data['patterns'].apply(lambda x: isinstance(x, str) and user_input in x.lower())]
    if not tag_matches.empty:
        tag = tag_matches.iloc[0]['tag']
        responses = tag_matches.iloc[0]['responses']
        responses = ast.literal_eval(responses)
        response = random.choice(responses)
        if isinstance(response, list):
            response = random.choice(response)
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "I'm sorry, I don't have a response for that.")


bot.polling()
