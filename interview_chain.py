from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from utils import OPENAI_API_KEY

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model="llama-3.1-8b-instant"
)

template = """
You are an interviewer for Indian tech companies.

Evaluate the following answer.

Give:
1. Score out of 10
2. Strengths
3. Improvements
4. Better sample answer

Answer:
{answer}
"""

prompt = PromptTemplate(
    input_variables=["answer"],
    template=template
)

def evaluate_answer(answer):

    formatted_prompt = prompt.format(answer=answer)

    response = llm.invoke(formatted_prompt)

    return response.content