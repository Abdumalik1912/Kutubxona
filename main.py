from kitob import Kitob
from kutubxona import Kutubxona
kitob1 = Kitob("Ikki eshik orasi", "O'tkir Hoshimov")
kitob2 = Kitob("Mehrobdan Chayon", "Abdulla Qodiriy")
kitob3 = Kitob("Shaytanat", "Tohir Malik")
kitob4 = Kitob("O'tkan kunlar", "Abdulla Qodiriy")
kutubxona = Kutubxona()

kutubxona.add_book(kitob1, 0, "0C0", 0, 0)
kutubxona.add_book(kitob2, 0, "0C0", 0, 0)
kutubxona.contains(0, "0C0", 0, 0)
kutubxona.add_book(kitob3, 0, "0C0", 0, 1)
print(kutubxona.get_floor(kitob3))
print(kutubxona.get_floor(kitob2))
print(kutubxona.find("Shaytanat", "Tohir Malik"))
print(kutubxona.find("Garri Potter va Azkaban Mahbusi", "J. K. Rouling"))
kutubxona.get_books(0, "0C0")
