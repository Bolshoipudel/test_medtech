# LangChain Agent для анализа Titanic Dataset

LLM-агент на базе LangChain для анализа данных Titanic с использованием custom tools и Python REPL

## Возможности

- **Анализ данных**: выполнение pandas операций, а также Python-операции
- **3 Custom Tools**:
  - `get_current_time` - получение текущего времени
  - `get_dataset_summary` - детальная статистика по датасету
  - `get_survival_statistics` - анализ выживаемости пассажиров

## Структура проекта

```
langchain-agent/
├── agent.py              # класс TitanicAgent с pandas dataframe агентом
├── tools.py              # custom tools 
├── data_loader.py        # Загрузка Titanic dataset
├── examples.py           # демо-скрипт с шестью примерами запросов
├── requirements.txt     
├── Dockerfile            
├── docker-compose.yml    
├── .env.example       
├── .dockerignore        
└── data/                 # Директория с результатами работы агента (results.txt)
```

## Быстрый старт

### 1. Настройка API ключа

Добавить OpenAI API ключ в файл `.env`:

```
OPENAI_API_KEY=api_key
```

### 2. Запуск

```bash
docker compose up --build -d
```

Агент автоматически выполнит 6 демо-запросов. Результаты сохранятся в файл `data/results.txt`.

Также можно посмотреть логи контейнера:

```bash
docker logs -f titanic-agent
```
