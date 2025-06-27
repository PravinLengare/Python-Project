import os
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import langchain.chains
from langchain_ollama import ChatOllama

information = """Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman. He is known for his leadership of Tesla, SpaceX, X (formerly Twitter), and the Department of Government Efficiency (DOGE). Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He received bachelor's degrees from the University of Pennsylvania in 1997 before moving to California, United States, to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became an American citizen.
                """
if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
   write me song on pizza
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))  # Here we have combining the  two things llm and summary_prompt_template a
    # Tem para decides how creative the language will be..
    llm=ChatOllama(model = "mistral")

    chain = summary_prompt_template | llm | StrOutputParser() # we have use pipe operator to combine

    res = chain.invoke(input={"information":information}) # we will run the chain using .invoke method
    print(res)  #If we want to run using api key
    # mock_output = {
    #     "content": """1. Elon Musk is a visionary entrepreneur leading Tesla, SpaceX, and X.
    # 2. Interesting facts:
    #    - He co-founded X.com which later became PayPal.
    #    - As of 2025, he is estimated to be worth $424.7 billion."""
    # }
    # print(mock_output["content"])
    # This is without api key used in this program
