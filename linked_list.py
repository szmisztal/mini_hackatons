class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0

    def insert_at_beginning(self, data):
        """Wstaw nowy węzeł na początku listy."""
        if self.head:
            new_head = Node(data, self.head)
            self.head = new_head
        else:
            self.head = Node(data)
        self.list_size += 1

    def insert_at_end(self, data):
        """Dodaj nowy węzeł na końcu listy."""
        if self.head is None:
            self.head = Node(data)
        elif self.head is not None and self.tail is None:
            self.tail = Node(data)
            self.head.next = self.tail
        else:
            new_tail = Node(data)
            self.tail.next = new_tail
            self.tail = new_tail
        self.list_size += 1

    def insert_at_position(self, data, key):
        """Wstaw nowy węzeł za określonym key (gdzie key, to wartość."""
        save_actually_head = self.head
        try:
            for _ in range(self.list_size):
                if self.head.data == key:
                    new_node = Node(data)
                    if self.head == self.tail:
                        self.head.next = new_node
                        self.tail = new_node
                    else:
                        new_node.next = self.head.next
                        self.head.next = new_node
                    self.list_size += 1
                    break
                else:
                    self.head = self.head.next
            self.head = save_actually_head
        except Exception:
            self.head = save_actually_head

    def delete_from_beginning(self):
        """Usuń węzeł z początku listy."""
        if self.list_size <= 1:
            self.clear()
        elif self.list_size == 2:
            self.head = self.tail
            self.tail = None
            self.list_size = 1
        else:
            self.head = self.head.next
            self.list_size -= 1

    def delete_from_end(self):
        """Usuń węzeł z końca listy."""
        if self.list_size <= 1:
            self.clear()
        elif self.list_size == 2:
            self.head.next = None
            self.tail = None
            self.list_size = 1
        else:
            save_actually_head = self.head
            for _ in range(self.list_size):
                if self.head.next == self.tail:
                    self.tail = self.head
                    self.tail.next = None
                else:
                    self.head = self.head.next
            self.head = save_actually_head
            self.list_size -= 1

    def delete_node(self, key):
        """Usuń węzeł zawierający określone dane."""
        if self.head.data == key:
            return self.delete_from_beginning()
        if self.tail is not None and self.tail.data == key:
            return self.delete_from_end()
        save_actually_head = self.head
        try:
            for _ in range(self.list_size):
                if self.head.next.data == key:
                    self.head.next = self.head.next.next
                    self.list_size -= 1
                else:
                    self.head = self.head.next
            self.head = save_actually_head
        except AttributeError:
            self.head =save_actually_head

    def search(self, key):
        """Znajdź węzeł zawierający dane, zwróć referencję do węzła lub None."""
        save_actually_head = self.head
        for _ in range(self.list_size):
            if self.head.data == key:
                return self.head
            self.head = self.head.next
        self.head = save_actually_head
        return None

    def display(self):
        """Wyświetl wszystkie elementy listy."""
        save_actually_head = self.head
        for _ in range(self.list_size):
            print(self.head.data)
            self.head = self.head.next
        self.head = save_actually_head

    def clear(self):
        """Usuń wszystkie węzły z listy, czyści listę."""
        self.head, self.tail, self.list_size = None, None, 0

    def size(self):
        """Zwróć liczbę węzłów w liście."""
        return self.list_size

