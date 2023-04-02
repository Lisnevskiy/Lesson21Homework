from classes.abstract_storage import Storage


class Shop(Storage):
    def __init__(self, capacity=20, item_limit=5):
        self.items = {}
        self.capacity = capacity
        self.item_limit = item_limit

    def add(self, item, quantity):
        if item not in self.items:
            if self.get_unique_items_count() >= self.item_limit:
                return '\nТовар невозможно добавить. Лимит уникальных товаров превышен!\n'

        if self.get_free_space() < quantity:
            return f'\nТовар не может быть добавлен, так как есть место только на {self.get_free_space()} товаров!\n'

        if item in self.items:
            self.items[item] += quantity
            return True
        else:
            self.items[item] = quantity
            return True

    def remove(self, item, quantity):
        if item not in self.items:
            return '\nТакого товара нет!\n'

        if self.items[item] < quantity:
            return f'\nНедостаточно {item}!\n'

        self.items[item] -= quantity

        if self.items[item] == 0:
            del self.items[item]

        return True

    def get_free_space(self):
        return self.capacity - sum(self.items.values())

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items.keys())
