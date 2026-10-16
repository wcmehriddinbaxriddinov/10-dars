from matplotlib import pyplot as plt

tillar = ["Python", "C", "JavaScript", "Java"]
oquvchilar = [15, 8, 12, 5]

plt.pie(oquvchilar, labels=tillar, autopct="%1.1f%%")

plt.title("O'quvchilarning sevimli dasturlash tillari")

plt.axis("equal")

plt.show()