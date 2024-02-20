from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(model = "mistral-openorca")

prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"topic": "Dogs"}))