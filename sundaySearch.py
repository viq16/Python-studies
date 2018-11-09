import random
import matplotlib.pyplot as mplib
import string as string

count = 0
counter = 0

def match_at(text,pattern,start):
    global counter
    for i in range(len(pattern)):
        counter += 1
        if text[start+i] != pattern[i]:
            return False
    return True


def naive_search(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if match_at(text, pattern, i):
            #print(f'Found at {i} :\n{text[:i] + pattern.upper() + text[i+len(pattern):]}\n' + i * ' ' + '^')
            pass


def constructRandomNString(n, character_set = string.ascii_lowercase):
    final_string = ""
    for _ in range(n):
        final_string += random.choice(character_set)
    return final_string

def generateRandomAlphabet(n, character_set = string.ascii_lowercase):
    final_string = ""
    for _ in range(n):
        new_letter = random.choice(character_set)
        while new_letter in final_string:
            new_letter = random.choice(character_set)
        final_string += random.choice(character_set)
    return final_string

def test_algorithm(text, pattern, algorithm):
    global counter
    counter = 0
    algorithm(text, pattern)
    return counter

def getLastIndices(pattern):
    lastIndices = {}
    for i in range(len(pattern)):
        lastIndices[pattern[i]] = i
    return lastIndices

def sunday_algorithm(text, pattern):
    global counter
    text_index = 0
    lastIndices = getLastIndices(pattern)
    while text_index < len(text) - len(pattern):
        if match_at(text, pattern, text_index):
            pass
        text_index += len(pattern)
        if text_index < len(text):
            text_index -= lastIndices.get(text[text_index], -1)



#text length test
SAMPLE_SIZE = 2
alphabet = string.ascii_lowercase[:4]
pattern = constructRandomNString(5, alphabet)
x = []
y_naive_search = []
y_sunday_search = []

for text_size in range(1, 1000000, 50000):
    x.append(text_size)
    naive_search_result = 0
    sunday_search_result = 0
    for _ in range(SAMPLE_SIZE):
        text = constructRandomNString(text_size, alphabet)
        naive_search_result += test_algorithm(text, pattern, naive_search)
        sunday_search_result += test_algorithm(text, pattern, sunday_algorithm)
    naive_search_result /= SAMPLE_SIZE
    sunday_search_result /= SAMPLE_SIZE
    y_naive_search.append(naive_search_result)
    y_sunday_search.append(sunday_search_result)
    print(text_size)

mplib.subplot(5,1,1)
mplib.plot(x, y_naive_search, label='naive')
mplib.plot(x, y_sunday_search, label='sunday')
mplib.xlabel('Text Length')
mplib.ylabel('Comparison Count')
mplib.title('Pattern Length - 5, Alphabet Length - 4')
mplib.legend()
mplib.grid(True)


#pattern length 
alphabet = string.ascii_lowercase[:4]
text = constructRandomNString(1000000, alphabet)
x = []
y_naive_search = []
y_sunday_search = []

for pattern_size in range(1, 1000000, 50000):   
    x.append(pattern_size)
    naive_search_result = 0
    sunday_search_result = 0
    for _ in range(SAMPLE_SIZE):
        pattern = constructRandomNString(pattern_size, alphabet)
        naive_search_result += test_algorithm(text, pattern, naive_search)
        sunday_search_result += test_algorithm(text, pattern, sunday_algorithm)
    naive_search_result /= SAMPLE_SIZE
    sunday_search_result /= SAMPLE_SIZE
    y_naive_search.append(naive_search_result)
    y_sunday_search.append(sunday_search_result)
    print(pattern_size)

mplib.subplot(5,1,3)
mplib.plot(x, y_naive_search, label='naive')
mplib.plot(x, y_sunday_search, label='sunday')
mplib.xlabel('Pattern Length')
mplib.ylabel('Comparison Count')
mplib.title('Text Length - 1000000, Alphabet Length - 4')
mplib.legend()
mplib.grid(True)



#alphabet length 

x = []
y_naive_search = []
y_sunday_search = []

for alphabet_size in range(1, 24, 1):
    x.append(alphabet_size)
    naive_search_result = 0
    sunday_search_result = 0
    for _ in range(SAMPLE_SIZE):
        alphabet = generateRandomAlphabet(alphabet_size, string.ascii_lowercase)
        pattern = constructRandomNString(30, alphabet)
        text = constructRandomNString(1000000, alphabet)
        naive_search_result += test_algorithm(text, pattern, naive_search)
        sunday_search_result += test_algorithm(text, pattern, sunday_algorithm)
    naive_search_result /= SAMPLE_SIZE
    sunday_search_result /= SAMPLE_SIZE
    y_naive_search.append(naive_search_result)
    y_sunday_search.append(sunday_search_result)
    print(alphabet_size)

mplib.subplot(5,1,5)
mplib.plot(x, y_naive_search, label='naive')
mplib.plot(x, y_sunday_search, label='sunday')
mplib.xlabel('Alphabet Length')
mplib.ylabel('Comparison Count')
mplib.title('Text Length - 1000000, Pattern Length - 30')
mplib.legend()
mplib.grid(True)
mplib.show()

