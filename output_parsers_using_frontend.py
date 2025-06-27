from typing import Tuple

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from output_parsers import summary_parser, Summary
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_agent_lookup import lookup as linkedin_lookup_agent  # optional

def ice_break_with(name:str)->Tuple[Summary, str]:


    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)
    summary_template = """
          Given the LinkedIn information {information} about a person, I want you to create:
          1. A short summary
          2. Two interesting facts about them
          \n{format_instructions}
       """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,partial_variables={"format_instructions":summary_parser.get_format_instructions()}
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
    )

    #chain = summary_prompt_template | llm
    chain = summary_prompt_template | llm | summary_parser

    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
    )

    res:Summary = chain.invoke({"information": linkedin_data})

    return res,linkedin_data.get("photoUrl")

if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Eden Marco")


