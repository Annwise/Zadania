class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def get_count():
        return Counter.count


obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
print(Counter.get_count())
