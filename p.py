from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

# Load .env file
load_dotenv()

# Initialize LLM (you can use GPT-4o, GPT-4-turbo, etc.)
llm = ChatOpenAI(model="gpt-4o")

# First Prompt: Extract topic
prompt_1 = PromptTemplate(
    input_variables=["text"],
    template="Extract the main topic from this text:\n{text}"
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1)

# Second Prompt: Generate question from topic
prompt_2 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a question about this topic: {topic}"
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2)

# Now run chain 1
text = "Elon Musk founded SpaceX and Tesla. He is known for space exploration."
topic = chain_1.run(text)

# Now run chain 2 using output from chain 1
question = chain_2.run(topic)

print("Generated Question:", question)
