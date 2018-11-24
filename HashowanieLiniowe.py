class EmptyCell: pass

class HashowanieLiniowe:
    def __init__(self, n=10000):
        self.n = n
        self.dane = [EmptyCell for _ in range(n)]

    def _hash(self, object):
        return abs(hash(object)) % self.n

    def insert(self, object):
        hash_code = self._hash(object)
        if self.is_empty_cell(hash_code):
            self.dane[hash_code]=object
        else:
            self.insert_duplicate_hash(object, hash_code)

    def insert_duplicate_hash(self, object, hash_code):
        new_hash_code = hash_code + 1
        if new_hash_code == self.n:
            new_hash_code = 0
        for i in range(self.n):
            if self.is_empty_cell(new_hash_code):
                self.dane[new_hash_code]=object
                break
            new_hash_code += 1
            if new_hash_code == self.n:
                new_hash_code = 0

    def is_empty_cell(self, index):
        if self.dane[index] is EmptyCell:
            return True
        return False

    def is_exist(self, object):
        hash_code = self._hash(object)
        for _ in range(self.n):
            if not self.is_empty_cell(hash_code):
                if self.dane[hash_code] == object:
                    return True, hash_code
            hash_code += 1
            if hash_code == self.n:
                hash_code = 0
        return False, hash_code


    def find(self, object):
        new_object = object
        index = self._hash(object)
        while self.dane[index] is not EmptyCell:
            if self.dane[index] == object:
                return index
            else:
                new_object+=1
                index = self._hash(new_object)
        return -1

    def delete(self, element):
        data_len = len(self.dane)
        index0 = self.find(element)
        if index0 != -1:
            self.dane[index0] = EmptyCell
        else:
            return

        index = index0 + 1
        if index >= data_len:
            index=0
        while self.dane[index] is not EmptyCell:
            elem = self.dane[index]
            elem_hash = self._hash(elem)
            if elem_hash != index:
                self.dane[index] = EmptyCell
                self.insert(elem)
            index += 1
            if index > data_len - 1:
                index = 0


