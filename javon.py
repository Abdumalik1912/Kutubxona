from kitob import Kitob


class Javon:

    def __init__(self):
        self._kitoblar = ["", "", "", "", "", "", "", "", "", ""]

    @property
    def kitoblar(self):
        return self._kitoblar

    def add_book(self, kitob: Kitob, num):
        if self._kitoblar[num] == "":
            self._kitoblar[num] = kitob
        else:
            print("Bu joyda kitob mavjud.")

    def contains(self, position):
        if self._kitoblar[position] == "":
            print("Bu joy bo'sh.")
        else:
            print("Bu joy bo'sh emas.")

    def get_books(self):
        for kitob in self._kitoblar:
            if kitob != "":
                print(kitob.to_string())

    def empty_shelf(self):
        for pos in self._kitoblar:
            if type(pos) == Kitob:
                return False
        return True

    def get_book_pos(self, kitob: Kitob):
        for i in range(len(self._kitoblar)):
            if self._kitoblar[i] == kitob:
                return i
        return -1

    def get_book(self, kitob_nomi, muallif):
        for kitob in self._kitoblar:
            try:
                if kitob.nom_property == kitob_nomi and kitob.muallif_property == muallif:
                    return kitob
            except AttributeError:
                pass
        return -1
