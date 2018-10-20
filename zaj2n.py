counter = 0

def match_at(T, w, i):
    global counter
    for j in range (0, len(w)):
        counter += 1 
        if T[i+j] != w[j]:
            return False
        return True
        
def naive_search(T, w):
    for i in range(0, len(T)-len(w)+1):
        #if match_at(T, w, i):
        if stringChain[i:i+len(w)] == w:
            print("found at index {}".format(i) + " : "+ stringChain[0:i].lower() + stringChain[i:i+len(w)].upper() + stringChain[i+len(w):len(T)].lower()
                  + "\n" + stringChain.upper() + "\n" + " "*i + "^")
            
    #swapCase method to convert big->small small->big letters
            
stringKey="kj"
stringChain="awdjwkjekeyaofhiwkjhjaekwoi"
naive_search(stringChain, stringKey)
#print("\nAll comparisons: " + str(counter))
#print("\n"+ stringChain[2:5:2])
print("\n"+ stringChain[::-1]) #reversed chain
print("\n"+ stringChain[::-2]) #rev, with interval: 2

#random package - generate random string with only lower() letters