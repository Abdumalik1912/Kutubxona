from javon import Javon
from kitob import Kitob

class Shkaf:

    def __init__(self, u_id):
        self._id = u_id
        self._javonlar = []
        self.add_javon()

    @property
    def u_id(self):
        return self._id

    @u_id.setter
    def u_id(self, new_id):
        self._id = new_id

    @property
    def javonlar(self):
        return self._javonlar

    def add_javon(self):
        for i in range(6):
            self._javonlar.append(Javon())

    def add_book(self, book: Kitob, javon_num, pos):
        self._javonlar[javon_num].add_book(book, pos)

    def contains(self, javon_num, position):
        self._javonlar[javon_num].contains(position)

    def get_books(self):
        count = 0
        for javon in self._javonlar:
            count += 1
            print(f"Shelf {count}")
            if javon.empty_shelf():
                print("Javon bo'sh.")
            else:
                javon.get_books()

    def get_shelf(self, kitob: Kitob):
        for i in range(len(self._javonlar)):
            javon_n = self._javonlar[i].get_book_pos(kitob)
            if javon_n != -1:
                return f"javon raqami: {i}, kitob joyi: {javon_n}"
        return -1

    def get_book(self, kitob_nomi, muallif):
        for javon in self._javonlar:
            kitob = javon.get_book(kitob_nomi, muallif)
            if kitob != -1:
                return kitob
        return -1



