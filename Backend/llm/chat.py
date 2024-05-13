from langchain_core.language_models.llms import LLM
from langchain_core.messages.system import SystemMessage
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)


def build(name: str, llm: LLM):
    # Load the prompt content
    with open(f'./prompts/{name}.txt', 'r', encoding='utf-8') as f:
        content = f.read()

    # Create a prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=content),
            HumanMessagePromptTemplate.from_template('{input_context}'),
        ]
    )

    # Attach an output parser
    output_parser = StrOutputParser()

    # Create a LLM chain with given content
    return prompt | llm | output_parser
