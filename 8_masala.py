from matplotlib import pyplot as plt

soat = [1, 2, 3, 4, 5, 6, 7]
ball = [40, 48, 55, 65, 72, 85, 90]

plt.scatter(soat, ball, color="blue", s=100)

plt.title("O'qish vaqti va test bali")
plt.xlabel("Tayyorlanish vaqti (soat)")
plt.ylabel("Test bali")

plt.grid()

plt.show()