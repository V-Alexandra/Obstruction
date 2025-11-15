class Iterator:
    def __init__(self, collection):
        self.__collection = collection
        self.__position = 0
    def __next__(self):
        if self.__position == len(self.__collection.data):
            raise StopIteration
        self.__position += 1
        return self.__collection.data[self.__position - 1]

class Collection:
    def __init__(self, data = []):
        self.__data = data
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, other):
        self.__data = other
    def append(self, value):
        self.__data.append(value)
    def __len__(self):
        return len(self.__data)
    def __iter__(self):
        return Iterator(self)
    def __setitem__(self, key, value):
        self.__data[key] = value
    def __getitem__(self, key):
        return self.__data[key]
    def __delitem__(self, key):
        del self.__data[key]
    def __str__(self):
        return str(self.__data)
