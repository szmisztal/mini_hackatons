class HashTable:
    def __init__(self, size = 10):
        self.size = size
        # Inicjalizacja tablicy (będącej listą list dla obsługi kolizji metodą łańcuchową)
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Metoda do obliczania indeksu w tablicy dla danego klucza
        pass

    def insert(self, key, value):
        # Metoda do dodawania pary klucz-wartość do tablicy haszującej
        pass

    def remove(self, key):
        # Metoda do usuwania pary klucz-wartość na podstawie klucza
        pass

    def search(self, key):
        # Metoda do wyszukiwania wartości na podstawie klucza
        pass

    def contains(self, key):
        # Metoda do sprawdzania, czy klucz znajduje się w tablicy
        pass

    def count_elements(self):
        # Metoda do zwracania liczby elementów w tablicy
        pass

# Przykład użycia (będzie wymagał implementacji metod)
hash_table = HashTable(size = 10)
hash_table.insert("klucz1", "wartość1")
print(hash_table.search("klucz1"))
hash_table.remove("klucz1")
print(hash_table.contains("klucz1"))
print(hash_table.count_elements())

hash_value = hash("przykładowy_tekst")

