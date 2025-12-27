from agent import TitanicAgent
from datetime import datetime
import os


def main():
    agent = TitanicAgent()

    output_file = "data/results.txt"
    os.makedirs("data", exist_ok=True)

    examples = [
        "Сколько строк в датасете и сколько сейчас времени?",
        "Покажи общую статистику по датасету",
        "Какая выживаемость была среди пассажиров разных классов?",
        "Найди средний возраст выживших и погибших пассажиров",
        "Сколько было мужчин и женщин на борту?",
        "Какая средняя цена билета у пассажиров 1-го класса?"
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# Результаты работы LangChain Agent\n")
        f.write(f"# Дата запуска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"{'=' * 80}\n\n")

        for i, query in enumerate(examples, 1):
            header = f"\n\n{'#' * 80}\nПример {i}/{len(examples)}\n{'#' * 80}\n\nЗапрос: {query}\n\n{'-' * 80}"
            print(header)
            f.write(header + "\n")

            answer = agent.query(query)

            footer = f"{'-' * 80}\n\nОтвет: {answer}\n"
            print(footer)
            f.write(footer + "\n")

    print(f"\n\n{'=' * 80}")
    print(f"Результаты сохранены в файл: {output_file}")
    print(f"{'=' * 80}\n")
        
if __name__ == "__main__":
    main()