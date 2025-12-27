import os
import logging
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from tools import get_current_time, get_dataset_summary, get_survival_statistics
from data_loader import load_titanic_data


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TitanicAgent:
    def __init__(self, openai_api_key=None):
        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY не найден в переменных окружения или параметрах")

        self.llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.3, max_tokens=500, api_key=self.api_key)
        self.df = load_titanic_data()
        self.agent = self._create_agent()

        logger.info("TitanicAgent инициализирован успешно")

    def _create_agent(self):
        extra_tools = [
            get_current_time,
            get_dataset_summary,
            get_survival_statistics
        ]

        return create_pandas_dataframe_agent(
            self.llm,
            self.df,
            extra_tools=extra_tools,
            verbose=True,
            agent_type="openai-functions",
            allow_dangerous_code=True,
            prefix="Ты выступаешь в роли ассистента, который анализирует датасет Titanic. Отвечай на русском языке."
        )

    def query(self, question):
        logger.info(f"Обработка запроса: {question}")
        result = self.agent.invoke(question)
        return result["output"]
