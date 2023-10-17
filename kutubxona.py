from qavat import Qavat
from kitob import Kitob


class Kutubxona:

    def __init__(self):
        self._qavatlar = []
        self.add_qavatlar()

    def add_qavatlar(self):
        for i in range(3):
            self._qavatlar.append(Qavat(i))

    def add_book(self, book: Kitob, qavat_num, shkaf_id, javon_num, pos):
        self._qavatlar[qavat_num].add_book(book, shkaf_id, javon_num, pos)

    def contains(self, qavat_num, shkaf_id, javon_num, position):
        self._qavatlar[qavat_num].contains(shkaf_id, javon_num, position)

    def get_books(self, qavat_num, shkaf_id):
        self._qavatlar[qavat_num].get_books(shkaf_id)

    def get_floor(self, kitob: Kitob):
        for i in range(len(self._qavatlar)):
            floor_n = self._qavatlar[i].get_closet(kitob)
            if floor_n != -1:
                return f"{kitob.to_string()} asari joyi: qavat raqami: {i}, {floor_n}"
        return "Ushbu kitob mavjud emas."

    def find(self, kitob_nomi, muallif):
        for qavat in self._qavatlar:
            kitob = qavat.get_book(kitob_nomi, muallif)
            if kitob != -1:
                return kitob
        return f"{muallif} qalamiga mansub {kitob_nomi} kitobi mavjud emas."

