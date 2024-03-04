import datetime


class Queue:
    def __init__(self):
        self.elements_list = []

    def add_item(self, item):
        self.elements_list.append(item)

    def get_item_with_highest_priority_and_delete_it(self):
        sorted_elements_list_by_priority = sorted(self.elements_list, key = lambda x: x.priority, reverse = True)
        return sorted_elements_list_by_priority.pop(0)

    def get_one_item(self, index):
        return self.elements_list[index]

    def check_list_is_empty(self):
        if len(self.elements_list) == 0:
            return True
        else:
            return False

    def count_items(self):
        return len(self.elements_list)


class Element:
    def __init__(self, priority):
        self.priority = int(priority)
        self.appearance_time = datetime.datetime.now()

    def __repr__(self):
        return f"Element with {self.priority}-priority"


queue = Queue()
one = Element(1)
two = Element(2)
three = Element(3)
queue.add_item(one)
queue.add_item(two)
queue.add_item(three)
print(queue.get_item_with_highest_priority_and_delete_it())
