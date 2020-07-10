"""
>>> store = Store()
>>> item = Item(name="Oreo Biscuits", price=30, category="Food")
>>> store.add_item(item)
>>> item = Item(name="Boost Biscuits", price=20, category="Food")
>>> store.add_item(item)
>>> item = Item(name="ParleG Biscuits", price=10, category="Food")
>>> store.add_item(item)
>>> store.display_all_items()
'Oreo Biscuits@30-Food\nBoost Biscuits@20-Food\nParleG Biscuits@10-Food'
>>> query = Query(field="price", operation="GT", value=15)
>>> results = store.exclude(query)  # exclude all items whose price is greater than 15
>>> results.display_all_items()
'ParleG Biscuits@10-Food'
"""


class Item:
    def __init__(self, name, price, category):
        if price<=0:
            raise ValueError("Invalid value for price, got "+ str(price))
        else:
            self.name = name
            self.price = price
            self.category = category
    def get_detail(self):
        return str(self.name)+'@'+str(self.price)+'-'+str(self.category)


class Query:
    operations = ['EQ','GT','GTE','LT','LTE','IN']
    def __init__(self, field, operation, value):
        if operation not in self.operations:
            raise ValueError('Invalid value for operation, got '+str(operation))
        else:
            self.field = field
            self.operation = operation
            self.value = value
    def get_detail(self):
        return str(self.field)+' '+str(self.operation)+' '+str(self.value)
    def match_item(self, item):
        operation = self.operation
        if operation == 'EQ':
            return getattr(item, self.field) == self.value
        elif operation == 'GT':
            return getattr(item, self.field) > self.value
        elif operation == 'GTE':
            return getattr(item, self.field) >= self.value
        elif operation == 'LT':
            return getattr(item, self.field) < self.value
        elif operation == 'LTE':
            return getattr(item, self.field) <= self.value
        elif operation == 'IN':
            return getattr(item, self.field) in self.value


class Store:
    def __init__(self):
        self.items = list()
    def add_item(self, item):
        self.items.append(item)
    def display_all_items(self):
        s = ''
        c = 1
        for i in self.items:
            if c<len(self.items):
                s += i.get_detail() + '\n'
                c += 1
            else:
                s += i.get_detail()
        return s
    def filter(self, query):
        store = Store()
        for item in self.items:
            if query.match_item(item):
                store.add_item(item)
        return store
    def exclude(self, query):
        store = Store()
        for item in self.items:
            if not query.match_item(item):
                store.add_item(item)
        return store


def default_test():
    store = Store()
    item = Item(name="Oreo Biscuits", price=30, category="Food")
    store.add_item(item)
    item = Item(name="Boost Biscuits", price=20, category="Food")
    store.add_item(item)
    display_all_items_check = store.display_all_items() == "Oreo Biscuits@30-Food\nBoost Biscuits@20-Food"
    if display_all_items_check:
        print('PASS')
    else:
        print('FAIL')
