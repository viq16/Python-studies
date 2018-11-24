class HashowanieLancuchowe:
    def __init__(self, n=10000):
        self.n = n
        self.dane = [[] for _ in range(n)]

    def _hash(self, object):
        return abs(hash(object)) % self.n

    def find(self, object):
        hash_code = self._hash(object)
        for v in self.dane[hash_code]:
            if v == object:
                return True, hash_code
        return False, hash_code

    def insert(self, object):
        self.dane[self._hash(object)].append(object)

    def delete(self, object):
        hash_code = self.find(object)
        if hash_code[0]:
            self.dane[hash_code[1]].remove(object)
