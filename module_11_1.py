import pandas as pd
import matplotlib.pyplot as plt

limons = pd.read_csv("limon_2.csv")
df = pd.DataFrame(limons)
df = df.sort_values("Время расчета", ascending=True)
df["Медиана"] = df["Средний Хешрейт В День"].median()
df1 = df.describe().round(2)
plt.xlabel('Время расчета')  # Подпись для оси х
plt.ylabel('Хэшрейт')  # Подпись для оси y
plt.title('График среднесуточного хэшрейта')  # Название
plt.plot(df["Время расчета"], df["Средний Хешрейт В День"], df["Медиана"])

plt.show()
print(df.to_string())
print()
print("Статистические параметры входных данных:")
print(df1.to_string())
