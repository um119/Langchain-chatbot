from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatOllama(
    model="minimax-m2.5:cloud",
    temperature=0.7
    )


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are an expert in {topic}, give consise, accurate answers"),
        ("human", "{question}")
    ])

chain= prompt | llm | StrOutputParser()


for chunk in chain.stream({"topic":"AI", "question":"what is rag and full form"}):
    print(chunk, end="", flush=True)


