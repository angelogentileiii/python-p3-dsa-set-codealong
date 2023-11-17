class MySet:
    def __init__(self, list = []):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True
        
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        return len(self.dictionary)
    

# bonuse tests

    # clear() is a standard method that removes all data from a dict
    def clear(self):
        self.dictionary.clear()
    
    def __str__(self):
        a_list = []
        for key, value in self.dictionary.items():
            a_list.append(str(key))
        return f'MySet: {{{",".join(a_list)}}}'

