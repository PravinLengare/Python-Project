import os
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from tools.tool import get_profile_url_tavily
# Make sure this returns a single URL string

load_dotenv()

def lookup(name: str) -> str:
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0,
        google_api_key=os.environ["GOOGLE_API_KEY"]  # ✅ Correct env variable
    )

    template = """Given the full name {name_of_person}, I want you to get me a link to their LinkedIn profile page.
                  Your answer should contain only a URL."""

    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url_tavily,  # ✅ Valid function
            description="Useful for when you need to get the LinkedIn Page URL of a person.",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name).to_string()}
    )

    return result["output"]
if __name__ == "__main__":
    linkedin_url=lookup("Eden Marco")
    print(linkedin_url)