import datetime
import random

class PriorityQueue:
    def __init__(self):
        self.elements_list = []

    def add_item(self, item):
        self.elements_list.append(item)

    def get_item_with_highest_priority_and_delete_it(self):
        check_list_is_empty = self.check_list_is_empty()
        if check_list_is_empty == False:
            sorted_elements_list_by_priority = sorted(self.elements_list, key = lambda x: x.priority, reverse = True)
            elements_with_highest_priority = []
            highest_priority = sorted_elements_list_by_priority[0].priority
            for element in sorted_elements_list_by_priority:
                if element.priority == highest_priority:
                    elements_with_highest_priority.append(element)
                else:
                    break
            sorted_elements_with_highest_priority_by_appearance_time = sorted(elements_with_highest_priority, key = lambda x: x.appearance_time)
            expected_element = sorted_elements_with_highest_priority_by_appearance_time[0]
            expected_element_index = self.elements_list.index(expected_element)
            return self.elements_list.pop(expected_element_index)
        else:
            return "List is empty"

    def show_one_item(self, index):
        try:
            check_list_is_empty = self.check_list_is_empty()
            if check_list_is_empty == False:
                return self.elements_list[index]
            else:
                return "List is empty"
        except IndexError as e:
            return e

    def check_list_is_empty(self):
        if self.count_items() == 0:
            return True
        else:
            return False

    def count_items(self):
        return len(self.elements_list)


class Element:
    def __init__(self, id, priority):
        self.id = id
        self.priority = int(priority)
        self.appearance_time = datetime.datetime.now()

    def __repr__(self):
        return f"Element_{self.id} with {self.priority}-priority, element appearance time = {self.appearance_time}"

# for testing
queue = PriorityQueue()
obj_1 = Element(len(queue.elements_list) + 1, random.randint(1, 10))
queue.add_item(obj_1)
obj_2 = Element(len(queue.elements_list) + 1, random.randint(1, 10))
queue.add_item(obj_2)
obj_3 = Element(len(queue.elements_list) + 1, random.randint(1, 10))
queue.add_item(obj_3)
obj_4 = Element(len(queue.elements_list)+ 1, random.randint(1, 10))
queue.add_item(obj_4)
obj_5 = Element(len(queue.elements_list) + 1, random.randint(1, 10))
queue.add_item(obj_5)
print(queue.elements_list)
print(queue.count_items())
print(queue.show_one_item(4))
print(queue.show_one_item(10))
print(queue.get_item_with_highest_priority_and_delete_it())
print(queue.count_items())

