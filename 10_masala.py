from matplotlib import pyplot as plt

ismlar = ["Ali", "Vali", "Sardor", "Malika", "Aziza", "Jasur"]
ballar = [78, 92, 65, 88, 95, 73]

plt.bar(ismlar, ballar, color="orange")

plt.title("O'quvchilar natijalari")
plt.xlabel("O'quvchilar")
plt.ylabel("Ballar")

plt.grid(axis="y", linestyle=":")

eng_yuqori = max(ballar)
eng_past = min(ballar)
ortacha = sum(ballar) / len(ballar)

print("Eng yuqori ball:", eng_yuqori)
print("Eng past ball:", eng_past)
print("O'rtacha ball:", ortacha)

plt.savefig("oquvchilar_natijasi.png")
plt.show()