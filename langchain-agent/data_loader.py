import logging
import pandas as pd

logger = logging.getLogger(__name__)

TITANIC_URL = "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/titanic.csv"
_df_cache = None


def load_titanic_data():
    global _df_cache
    if _df_cache is None:
        logger.info(f"Загрузка Titanic dataset с {TITANIC_URL}")
        _df_cache = pd.read_csv(TITANIC_URL)
        logger.info(f"Датасет загружен: {len(_df_cache)} строк")
    return _df_cache
