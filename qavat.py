from shkaf import Shkaf
from kitob import Kitob


class Qavat:

    def __init__(self, num):
        self._shkaflar = {}
        self.add_shkaf(num)

    @property
    def shkaflar(self):
        return self._shkaflar

    def add_shkaf(self, num):
        for i in range(30):
            n_id = f"{num}C{i}"
            self._shkaflar.update({n_id:  Shkaf(n_id)})

    def add_book(self, book: Kitob, shkaf_id, javon_num, pos):
        self._shkaflar[shkaf_id].add_book(book, javon_num, pos)

    def contains(self, shkaf_id, javon_num, position):
        self._shkaflar[shkaf_id].contains(javon_num, position)

    def get_books(self, shkaf_id):
        self._shkaflar[shkaf_id].get_books()

    def get_closet(self, kitob: Kitob):
        for c_id in self._shkaflar:
            shkaf_n = self._shkaflar[c_id].get_shelf(kitob)
            if shkaf_n != -1:
                return f"shkaf id: {c_id}, {shkaf_n}"
        return -1

    def get_book(self, kitob_nomi, muallif):
        for shkaf in self._shkaflar.values():
            kitob = shkaf.get_book(kitob_nomi, muallif)
            if kitob != -1:
                return kitob
        return -1
