import matplotlib.pyplot as plt
import numpy as np

y = np.loadtxt("data.txt")
settings = open("settings.txt", "r", encoding="utf-8")
T = 1 / float(settings.read().split()[0])
x = np.array([i for i in range(len(y))])
x = x * T
t_charge = round(x[y.argmax()], 2)
t_decharge = round(x[-1] - t_charge, 2)

y_max = y.max()
y_min = y.min()
x_max = x.max()
x_min = x.min()


fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, y, linestyle="-", color="darkgreen", linewidth=2, marker="D", markersize=5, markevery=[i for i in range(0, len(x), 5)], label="U(t)",
markerfacecolor="red")
ax.set_ylim(y_min, y_max + 0.05)
ax.set_xlim(x_min, x_max + 0.05)
ax.set_ylabel("Напряжение U, В")
ax.set_xlabel("Время t, с")
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепи (цепь была спаяна на занятии №6,\n данные были \
прочитаны на занятии №7)", wrap=True, loc="center")
ax.grid(b=True, which="major", linewidth=2, color="#708090", linestyle="--")
ax.grid(b=True, which="minor", linewidth=0.5, color="#D3D3D3", linestyle="dotted")
ax.text(4.2, 1.7, f"Время заряда: {t_charge} с", fontsize=10, color="black")
ax.text(4.2, 1.4, f"Время разряда: {t_decharge} с", fontsize=10, color="black")
ax.legend()
plt.savefig("voltage_time_graph.svg")
plt.show()