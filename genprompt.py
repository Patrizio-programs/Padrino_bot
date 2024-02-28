from langchain.prompts import (
    SystemMessagePromptTemplate,
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)


def generate_chat_prompt(system_message, human_message, bot, chat_id, message_id):
    # Create the system message prompt
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_message)
    # Create the human message prompt
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)
    # Combine the prompts into a chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # Format the chat prompt and convert it to messages
    messages = chat_prompt.format_prompt().to_messages()
    # Generate the response from the chatbot
    response = llm(str(chat_prompt.format_prompt()))
    return response

