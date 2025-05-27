import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear las carpetas necesarias
os.makedirs("files/images", exist_ok=True)

# Simular algunos datos de ejemplo
df = pd.DataFrame({
    'carrier': ['AA', 'AA', 'UA', 'UA', 'DL', 'DL'],
    'dep_delay': [10, 15, 5, 30, 20, 25],
    'day_of_week': ['Mon', 'Tue', 'Mon', 'Wed', 'Thu', 'Fri'],
    'hour': [8, 9, 8, 10, 11, 12]
})

# Gráfico 1: Retraso por aerolínea
df.groupby('carrier')['dep_delay'].mean().plot(kind='bar', title='Delay by Carrier')
plt.savefig("files/images/delays_by_carrier.png")
plt.clf()

# Gráfico 2: Retraso por día de la semana
df.groupby('day_of_week')['dep_delay'].mean().plot(kind='bar', title='Delay by Day of Week')
plt.savefig("files/images/delays_by_day_of_week.png")
plt.clf()

# Gráfico 3: Retraso por hora del día
df.groupby('hour')['dep_delay'].mean().plot(kind='bar', title='Delay by Hour of Day')
plt.savefig("files/images/delays_by_hour_of_day.png")
plt.clf()
