import os
import re

import pandas as pd
from huggingface_hub import hf_hub_download
from langchain import LLMChain, PromptTemplate
from langchain.agents.agent_types import AgentType
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.llms import LlamaCpp
from langchain_experimental.agents import create_csv_agent
from prompts import TEMPLATE


class Agent:
    def __init__(self, use_openai, csv_path):
        self.csv_path = csv_path
        if use_openai:
            self.use_openai = True
            llm = ChatOpenAI(
                openai_api_key=os.getenv("OPENAI_API_KEY"),
                model_name="gpt-3.5-turbo-1106",
            )

            self.agent = create_csv_agent(
                llm,
                self.csv_path,
                verbose=False,
                agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            )
        else:
            self.use_openai = False
            model_name_or_path = "TheBloke/Llama-2-13B-chat-GGML"
            model_basename = "llama-2-13b-chat.ggmlv3.q5_1.bin"
            model_path = hf_hub_download(
                repo_id=model_name_or_path, filename=model_basename
            )
            n_gpu_layers = 40
            n_batch = 512  # Should be between 1 and n_ctx, consider the amount of VRAM in your GPU.
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

            self.agent = LlamaCpp(
                model_path=model_path,
                max_tokens=1024,
                n_gpu_layers=n_gpu_layers,
                n_batch=n_batch,
                callback_manager=callback_manager,
                verbose=True,
                n_ctx=4096,  # Context window
                stop=["USER:"],  # Dynamic stopping when such token is detected.
                temperature=0,
            )

    def ask(self, question):
        if self.use_openai:
            answer = self.agent.run(question)
            return answer
        else:
            df = pd.read_csv(self.csv_path)
            prompt = PromptTemplate(template=TEMPLATE, input_variables=["question"])
            llm_chain = LLMChain(prompt=prompt, llm=self.agent)

            resp = llm_chain.run(question)
            parts = re.split("`", resp)
            answer = parts[0][8:] + str(eval(parts[1])) + "."
            return answer


# if __name__ == "__main__":
#    agent = Agent(use_openai=True, csv_path="listings.csv")
#    answer = agent.ask("¿Cuál es el precio promedio de los departamentos en venta?")
