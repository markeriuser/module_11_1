import pandas as pd

# 1. Чтение данных из CSV файла
df = pd.read_csv('data.csv')
print(df.head())  # Выводим первые 5 строк

# 2. Простой анализ данных (группировка и агрегация)
grouped = df.groupby('column_name').mean()  # Среднее значение по группам
print(grouped)

# 3. Фильтрация данных
filtered_data = df[df['column_name'] > 10]  # Фильтруем строки, где значение больше 10
print(filtered_data)
