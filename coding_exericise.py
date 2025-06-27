import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
print("Hello LangChain + Gemini")

information = """
Elon Musk is the CEO of Tesla and SpaceX. He co-founded X.com which became PayPal.
"""

prompt_template = """
Given the following information {information}, write:
1. A short summary.
2. Two interesting facts.
"""

prompt = PromptTemplate(
    input_variables=["information"],
    template=prompt_template
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-pro",  # ✅ use exactly as returned by list_models()
    temperature=0,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

chain = prompt | llm
response = chain.invoke({"information": information})
print(response.content)
