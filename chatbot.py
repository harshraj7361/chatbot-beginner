from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.8-flash",
    temperature = 0.5
    
)
chat_history= []

while True:
    user_input = input("YOU: " )
    
    if user_input == "exit" :
        break

    chat_history.append(HumanMessage(content=user_input))


    result=llm.invoke(user_input)
    chat_history.append(AIMessage(content=result.content))

    print("AI: ",result.content[0]["text"])

print(chat_history)