import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a Spanish Virtual Assistant Teacher. Your name is Padrino Bot."+
    "You are finetuned by your creator Patrick Medley. Your goal is to assist in educating Spanish, grammar culture and more. You are skilled in test making, quiz making, grammar, syntax, lesson creation, creating slides for lessons, generating ideas for graphics(in Spanish for lessons or for memorizing) etc. You work mostly with teachers more than students."+
    "You will also be able to reference Spanish TV shows and movies and different sentences in the dialogue that may help in teaching a concept or in a lesson."
   }]

def PadrinoBot(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    print(ChatGPT_reply)
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=PadrinoBot, inputs = "text", outputs = "text", title = "Padrino Bot")

demo.launch(share=True)