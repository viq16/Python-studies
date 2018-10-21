import random
import string
import matplotlib.pyplot as plt

def random_str(size, alphabet):
    result = ''
    for _ in range(size):
        result += random.choice(alphabet)
    return result

print(random_str(10, string.ascii_lowercase))

counter = 0

def match_at(T, w, i):
    global counter
    for j in range (0, len(w)):
        counter += 1 
        if T[i+j] != w[j]:
            return False
        return True
    
def naive_search(T, W):
    for i in range(len(T)-len(W)+1):
        if match_at(T,W,i):
            pass
        
        
        
def test_alg(T, W, alg):
    global counter
    counter=0
    alg(T,W)
    return counter

SAMPLE_SIZE = 10
A = string.ascii_lowercase[:4]
W = random_str(5, A)
x = []
y_naive_search = []
#y_sunday_search = [] #TODO
for T_size in range(1, 1000, 10):
    x.append(T_size)
    naive_search_res = 0
    #sunday_search_res = 0
    for _ in range(SAMPLE_SIZE):
        T = random_str(T_size, A)
        naive_search_res += test_alg(T, W, naive_search)
        #sunday_search_res += test_alg(T, W, sunday_search)
    naive_search_res /= SAMPLE_SIZE
    #sunday_search_res /= SAMPLE_SIZE
    y_naive_search.append(naive_search_res)
    #y_sunday_search.append(sunday_search_res)
  
plt.plot(x, y_naive_search, label = 'naive')
#plt.plot(x, y_sunday_search, label = 'sunday')
plt.xlabel('|T|')
plt.ylabel('liczba porownan')
plt.title("|W|=5, |A|=4")
plt.legend()
plt.show()


#Jupiter notebook 