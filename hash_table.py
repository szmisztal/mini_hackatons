class HashTable:
    def __init__(self, size = 10):
        self.size = size
        # Inicjalizacja tablicy (będącej listą list dla obsługi kolizji metodą łańcuchową)
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Metoda do obliczania indeksu w tablicy dla danego klucza
        index = hash(key) % self.size
        return index

    def insert(self, key, value):
        # Metoda do dodawania pary klucz-wartość do tablicy haszującej
        index = self.hash_function(key)
        checking_if_the_key_exists = self.contains(key)
        if checking_if_the_key_exists is True:
            for item in self.table[index]:
                for item_key in item.keys():
                    if key == item_key:
                        item[key] = value
        else:
            self.table[index].append({key: value})

    def remove(self, key):
        # Metoda do usuwania pary klucz-wartość na podstawie klucza
        index = self.hash_function(key)
        checking_if_the_key_exists = self.contains(key)
        if checking_if_the_key_exists is True:
            for item in self.table[index]:
                for item_key in item.keys():
                    if key == item_key:
                        self.table[index].remove(item)
                        break
        else:
            return None

    def search(self, key):
        # Metoda do wyszukiwania wartości na podstawie klucza
        index = self.hash_function(key)
        checking_if_the_key_exists = self.contains(key)
        if checking_if_the_key_exists is True:
            for item in self.table[index]:
                for item_key in item.keys():
                    if key == item_key:
                        return item[key]
        else:
            return None

    def contains(self, key):
        # Metoda do sprawdzania, czy klucz znajduje się w tablicy
        index = self.hash_function(key)
        if len(self.table[index]) > 0:
            for item in self.table[index]:
                if key in item.keys():
                    return True
            else:
                return False
        else:
            return False

    def count_elements(self):
        # Metoda do zwracania liczby elementów w tablicy
        pairs_number = 0
        for list in self.table:
            pairs_number += len(list)
        return pairs_number


# Przykład użycia (będzie wymagał implementacji metod)
hash_table = HashTable(size = 10)
hash_table.insert("klucz1", "wartość1")
print(hash_table.search("klucz1"))
hash_table.remove("klucz1")
print(hash_table.contains("klucz1"))
print(hash_table.count_elements())


