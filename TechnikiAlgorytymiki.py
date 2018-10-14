def find(T, v):
    for i in range(len(T)):
        print("Przejscie petli nr: " + str(i+1))
        if T[i] == v: return True
    return False


def find_min(T, f):
    r=f
    for i in range(f + 1, len(T)):
        if T[i] < T[r]: r = i
    return r

def find_max(T, f):
    r=f
    for i in range(f + 1, len(T)):
        if T[i] > T[r]: r = i
    return r

print(find([5, 7, 11, 31, 2], 31))

print(find_min([5, 7, 11, 31, 2], 2))

print("-------------------")

def sort(T):
    for i in range(len(T)):
        m = find_min(T, i)
        T[i], T[m] = T[m], T[i]
    return T

def sort2(T):
    for i in range(len(T)):
        m = find_max(T, i)
        T[i], T[m] = T[m], T[i]
    return T
print([4, 2, 6, 12, 7, 9, 69, 15])
print(sort([4, 2, 6, 12, 7, 9, 69, 15]))
print(sort2([4, 2, 6, 12, 7, 9, 69, 15]))

class klasa:
    rozmiar = 2
    dlugosc = 3

t = klasa()
print(str(t.rozmiar) + ":" + str(t.dlugosc))
