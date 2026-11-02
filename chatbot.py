from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(
    model = "llama3.2",
    temperature = 0.5
    
)
chat_history= []

while True:
    user_input = input("YOU: " )
    
    if user_input == "exit" :
        break

    chat_history.append(HumanMessage(content=user_input))


    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))

    print("AI: ",result.content)

print(chat_history)