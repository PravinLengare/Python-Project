import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")


    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them 
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo",openai_api_key=os.getenv("OPENAI_API_KEY"))  # Here we have combining the  two things llm and summary_prompt_template a
    # Tem para decides how creative the language will be..

    chain = summary_prompt_template | llm  # we have use pipe operator to combine

    # res = chain.invoke(input={"information":information}) # we will run the chain using .invoke method
    # print(res)  If we want to run using api key
    mock_output = {
        "content": """1. Elon Musk is a visionary entrepreneur leading Tesla, SpaceX, and X. 
    2. Interesting facts:
       - He co-founded X.com which later became PayPal.
       - As of 2025, he is estimated to be worth $424.7 billion."""
    }
    print(mock_output["content"])
    # This is without api key used in this program
