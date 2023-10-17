class Kitob:

    def __init__(self, nom, muallif):
        self._nom = nom
        self._muallif = muallif

    @property
    def nom_property(self):
        return self._nom

    @nom_property.setter
    def nom_property(self, yangi_nom):
        self._nom = yangi_nom

    @nom_property.deleter
    def nom_property(self):
        del self._nom

    @property
    def muallif_property(self):
        return self._muallif

    @muallif_property.setter
    def muallif_property(self, yangi_muallif):
        self._muallif = yangi_muallif

    @muallif_property.deleter
    def muallif_property(self):
        del self._muallif

    def to_string(self):
        return f"{self._nom}, {self._muallif}"
