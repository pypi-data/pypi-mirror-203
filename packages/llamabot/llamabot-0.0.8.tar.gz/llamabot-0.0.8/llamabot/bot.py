"""Bot abstractions that let me quickly build new GPT-based applications."""

import os
from pathlib import Path
from typing import List, Union

import openai
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.text_splitter import TokenTextSplitter
from llama_index import Document, GPTSimpleVectorIndex, LLMPredictor, ServiceContext
from llama_index.response.schema import Response

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


class SimpleBot:
    """Simple Bot that is primed with a system prompt, accepts a human message, and sends back a single response.

    This bot does not retain chat history.
    """

    def __init__(self, system_prompt, temperature=0.0, model_name="gpt-4"):
        """Initialize the SimpleBot.

        :param system_prompt: The system prompt to use.
        :param temperature: The model temperature to use.
            See https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature
            for more information.
        :param model_name: The name of the OpenAI model to use.
        """
        self.system_prompt = system_prompt
        self.model = ChatOpenAI(model_name=model_name, temperature=temperature)

    def __call__(self, human_message):
        """Call the SimpleBot.

        :param human_message: The human message to use.
        :return: The response to the human message, primed by the system prompt.
        """
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=human_message),
        ]
        return self.model(messages)


class ChatBot:
    """Chat Bot that is primed with a system prompt, accepts a human message.

    Automatic chat memory management happens.

    h/t Andrew Giessel/GPT4 for the idea.
    """

    def __init__(self, system_prompt, temperature=0.0, model_name="gpt-4"):
        """Initialize the ChatBot.

        :param system_prompt: The system prompt to use.
        :param temperature: The model temperature to use.
            See https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature
            for more information.
        :param model_name: The name of the OpenAI model to use.
        """
        self.model = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.chat_history = [SystemMessage(content=system_prompt)]

    def __call__(self, human_message) -> Response:
        """Call the ChatBot.

        :param human_message: The human message to use.
        :return: The response to the human message, primed by the system prompt.
        """
        self.chat_history.append(HumanMessage(content=human_message))
        response = self.model(self.chat_history)
        self.chat_history.append(response)
        return response

    def __repr__(self):
        """Return a string representation of the ChatBot.

        :return: A string representation of the ChatBot.
        """
        representation = ""

        for message in self.chat_history:
            if isinstance(message, SystemMessage):
                prefix = "[System]\n"
            elif isinstance(message, HumanMessage):
                prefix = "[Human]\n"
            elif isinstance(message, AIMessage):
                prefix = "[AI]\n"

            representation += f"{prefix}{message.content}" + "\n\n"
        return representation


class QueryBot:
    """QueryBot is a bot that lets us use GPT4 to query documents."""

    def __init__(
        self,
        system_message: str,
        model_name="gpt-4",
        temperature=0.0,
        doc_paths: List[Union[str, Path]] = None,
        saved_index_path: Union[str, Path] = None,
        chunk_size: int = 2000,
        chunk_overlap: int = 0,
    ):
        """Initialize QueryBot.

        Pass in either the doc_paths or saved_index_path to initialize the QueryBot.

        NOTE: QueryBot is not designed to have memory!

        The default text splitter is the TokenTextSplitter from LangChain.
        The default index that we use is the GPTSimpleVectorIndex from LlamaIndex.
        We also default to using GPT4 with temperature 0.0.

        :param system_message: The system message to send to the chatbot.
        :param model_name: The name of the OpenAI model to use.
        :param temperature: The model temperature to use.
            See https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature
            for more information.
        :param doc_paths: A list of paths to the documents to use for the chatbot.
            These are assumed to be plain text files.
        :param saved_index_path: The path to the saved index to use for the chatbot.
        :param chunk_size: The chunk size to use for the LlamaIndex TokenTextSplitter.
        :param chunk_overlap: The chunk overlap to use for the LlamaIndex TokenTextSplitter.
        """

        self.system_message = system_message

        chat = ChatOpenAI(model_name=model_name, temperature=temperature)
        llm_predictor = LLMPredictor(llm=chat)
        service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

        # Build index
        if saved_index_path is not None:
            index = GPTSimpleVectorIndex.load_from_disk(
                saved_index_path, service_context=service_context
            )

        else:
            self.doc_paths = doc_paths
            splitter = TokenTextSplitter(
                chunk_size=chunk_size, chunk_overlap=chunk_overlap
            )
            documents = []
            for fname in doc_paths:
                with open(fname, "r") as f:
                    docs = splitter.split_text(f.read())
                    documents.extend([Document(d) for d in docs])
            index = GPTSimpleVectorIndex.from_documents(
                documents, service_context=service_context
            )
        self.index = index

    def __call__(
        self, query: str, return_sources: bool = True, **kwargs
    ) -> Union[str, Response]:
        """Call the QueryBot.

        :param query: The query to send to the document index.
        :param return_sources: Whether to return the source nodes of the query.
            Defaults to True.
            If True, we return the Response object from LlamaIndex;
            if False, we simply return the text generated.
        :param kwargs: Additional keyword arguments to pass to the chatbot.
            These are passed into LlamaIndex's index.query() method.
            For example, if you want to change the number of documents consulted
            from the default value of 1 to n instead,
            you can pass in the keyword argument `similarity_top_k=n`.
        :return: The response to the query generated by GPT4.
        """
        q = ""
        q += self.system_message + "\n\n"
        q += query + "\n\n"
        result = self.index.query(q, **kwargs)
        if return_sources:
            return result
        return result.response

    def save(self, path: Union[str, Path]):
        """Save the QueryBot and index to disk.

        :param path: The path to save the QueryBot index.
        """
        path = Path(path)
        if not path.suffix == ".json":
            path = path.with_suffix(".json")
        self.index.save_to_disk(path)
