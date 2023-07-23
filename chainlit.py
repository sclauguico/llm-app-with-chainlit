# import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
import chainlit as cl
# from constants import openai_key

# os.environ["OPENAI_API_KEY"] = openai_key

template = """Question: {question}

Answer: Let's think step by step."""

@cl.langchain_factory(use_async=True)
def factory():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=ChatOpenAI(temperature=0, streaming=True))                     
    return llm_chain