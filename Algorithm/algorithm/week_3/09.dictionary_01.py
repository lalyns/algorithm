class Dict:
    def __init__(self):
        self.items = [None] * 8

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value
        return

    def get(self, key):
        index = hash(key) % len(self.items)
        if self.items[index] is None :
            return "not included index"
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!