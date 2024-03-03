import datetime


class Queue:
    def __init__(self):
        self.elements_list = []
    def add_item(self):
        pass

    def get_first_item_and_delete_it(self):
        pass

    def get_one_item(self, index):
        pass

    def check_list_is_empty(self):
        if len(self.elements_list) == 0:
            return True
        else:
            return False

    def count_items(self):
        return len(self.elements_list)


class Element:
    def __init__(self, priority):
        self.priority = priority
        self.appearance_time = datetime.datetime.now()
