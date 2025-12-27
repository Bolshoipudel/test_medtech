from datetime import datetime
from langchain.tools import tool
from data_loader import load_titanic_data

@tool
def get_current_time():
    """Возвращает текущее время"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#langchain требует docstrings...
@tool
def get_dataset_summary(df_name="titanic"):
    """Возвращает статистику по датасету"""
    if df_name != "titanic":
        return f"Датасет '{df_name}' не найден. Доступные датасеты: titanic"

    df = load_titanic_data()

    summary = f"""Сводка по датасету:
- Всего строк: {len(df)}
- Всего колонок: {len(df.columns)}
- Колонки: {', '.join(df.columns.tolist())}
- Пропущенные значения: {df.isnull().sum().sum()} всего"""

    return summary


@tool
def get_survival_statistics():
    """Возвращает статистику выживаемости пассажиров Titanic"""
    df = load_titanic_data()

    total = len(df)
    survived = df['Survived'].sum()
    survival_rate = (survived / total) * 100

    class_survival = df.groupby('Pclass')['Survived'].agg(['sum', 'count'])
    class_survival['rate'] = (class_survival['sum'] / class_survival['count']) * 100

    gender_survival = df.groupby('Sex')['Survived'].agg(['sum', 'count'])
    gender_survival['rate'] = (gender_survival['sum'] / gender_survival['count']) * 100

    stats = f"""Статистика выживаемости:
- Общая выживаемость: {survival_rate:.1f}% ({survived}/{total})
- По классам:
  * 1-й класс: {class_survival.loc[1, 'rate']:.1f}% ({int(class_survival.loc[1, 'sum'])}/{int(class_survival.loc[1, 'count'])})
  * 2-й класс: {class_survival.loc[2, 'rate']:.1f}% ({int(class_survival.loc[2, 'sum'])}/{int(class_survival.loc[2, 'count'])})
  * 3-й класс: {class_survival.loc[3, 'rate']:.1f}% ({int(class_survival.loc[3, 'sum'])}/{int(class_survival.loc[3, 'count'])})
- По полу:
  * Женщины: {gender_survival.loc['female', 'rate']:.1f}% ({int(gender_survival.loc['female', 'sum'])}/{int(gender_survival.loc['female', 'count'])})
  * Мужчины: {gender_survival.loc['male', 'rate']:.1f}% ({int(gender_survival.loc['male', 'sum'])}/{int(gender_survival.loc['male', 'count'])})"""

    return stats
