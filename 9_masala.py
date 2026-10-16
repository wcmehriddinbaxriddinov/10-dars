from matplotlib import pyplot as plt

kunlar = [1, 2, 3, 4, 5, 6, 7]
soat = [1, 2, 2, 3, 4, 3, 5]

plt.plot(kunlar, soat, color="blue", marker="o", linewidth=2)

plt.title("Haftalik dasturlash vaqti")
plt.xlabel("Kunlar")
plt.ylabel("Soat")

plt.grid()

plt.savefig("natija.png")

plt.show()