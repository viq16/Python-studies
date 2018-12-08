#jeśli   rodzic  jest    na  pozycji p,
#jego    lewe    dziecko ma  indeks  2p,
#a   jego    prawe   dziecko -   2p+ 1
#węzeł   na  pozycji n   ma  rodzica na  pozycji n//2
#klucz   węzła   x   jest    większy bądź
#równy   kluczowi    jego    rodzica p

class BinHeap:
    #w konstruktorze wstawiamy 0 jako pierwszy element listy
    def __init__(self):
        self.heapList=[0]
        self.currentSize=0
        
    def percUp(self,i):
        while   i//2 > 0: #dopóki istnieje rodzic 
            if  self.heapList[i] <= self.heapList[i//2]: #jeżeli ostatni + element mniejszy niż rodzic
                tmp=self.heapList[i//2] #zamiana węzła z rodzicem
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
        
        
    def insert(self,k):
        self.heapList.append(k) #dodanie elementu na koniec listy
        self.currentSize    =   self.currentSize+1
        self.percUp(self.currentSize) #poprawa kopca
            
    def findMin(self):
        return  self.heapList[1]
    
    def getRoot(self):
        return self.heapList[1]
        
#jeśli   porządek    został  zburzony,   przywracamy go, zamieniając korzeń
#z   mniejszym   z   jego    dzieci
#kontunuujemy    zamiany do  odzyskania  porządku    kopca
    def percDown(self,i):
        while(i*2)<=self.currentSize:
            mc=self.minChild(i)
            if  self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
                         
    def minChild(self,i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1
                  
    def delMin(self):
        if self.currentSize > 0:
            retval=self.heapList[1]
            self.heapList[1]=self.heapList[self.currentSize] #wstawiamy ostatni element z listy w miejsce korzenia
            self.currentSize=self.currentSize-1
            self.heapList.pop()
            self.percDown(1) #przywracanie porzadku kopca
            return  retval
        
    def buildHeap(self,alist):
        i=len(alist)//2
        self.currentSize=len(alist)-1
        self.heapList=alist[:]
        while(i>0):
            self.percDown(i)
            i=i-1
                
    def size(self):
        return  self.currentSize
                
    def isEmpty(self):
        print(self.currentSize == 0)
        return  self.currentSize == 0
            
    def __str__(self):
        size = self.currentSize
        txt = ""
        txt2 = ""
        lvl = 0
        tabIterator = 1
        x=1
        while x <= size:
            if lvl == 0:
                txt += "\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + str(self.heapList[x])
                x += 1
                lvl+=1
                txt += "\n"
            elif lvl == 1:
                if tabIterator == 1:
                    txt += tabIterator*"\t\t\t\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                else:
                    txt += tabIterator*"\t\t\t\t\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                x += 1
                if x > 3:
                    lvl+=1
                    txt += "\n"
                    tabIterator = 1
            elif lvl == 2:
                if tabIterator == 1:
                    txt += tabIterator*"\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator == 2:
                    txt += "\t\t\t\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator == 3:
                    txt += "\t\t\t\t\t\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                else:
                    txt += "\t\t\t\t\t\t" + str(self.heapList[x])
                    tabIterator +=1
                x += 1
                if x > 7:
                    lvl+=1
                    txt += "\n"
                    tabIterator = 1
            elif lvl == 3:
                if tabIterator==1 or tabIterator==2 or tabIterator==4 or tabIterator==6 or tabIterator==8:
                    txt2 += 2*"        " + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator==3 or tabIterator==7:
                    txt2 += 4*"        " + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator == 5:
                    txt2 += 6*"        " + str(self.heapList[x])
                    tabIterator +=1
                    print("JESTEM")
                print(tabIterator)
                x += 1
                if x > 15:
                    lvl+=1
                    txt2 += "\n"
                    tabIterator = 1
            elif lvl == 4:
                if tabIterator == 1:
                    txt2 += "\t\t" + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator in (2,4,6,10,13):
                    txt2 += "    " + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator in (3,7,9,12):
                    txt2 += "\t       " + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator in (5,11):
                    txt2 += "\t\t\t      " + str(self.heapList[x])
                    tabIterator +=1
                elif tabIterator == 8:
                    txt2 += "\t\t\t\t\t      " + str(self.heapList[x])
                    tabIterator +=1
                x += 1
                if x > 15:
                    lvl+=1
                    txt2 += "\n"
        #txt="{}".format(self.heapList[1:])
        return  txt + txt2

    def editNodeValueTest(self, index, newValue):
        if index > 0 and index < self.currentSize:
            print("przed zamiana: ")
            print(self)
            self.heapList[index] = newValue
            print("po zamianie: ")
            print(self)
            self.percDown(self.currentSize)
            self.buildHeap(self.heapList)
            print("po uporzadkowaniu: ")
            print(self)

    def editNodeValue(self, index, newValue):
        if index > 0 and index < self.currentSize:
            self.heapList[index] = newValue
            self.percDown(self.currentSize)
            self.buildHeap(self.heapList)
        
    def getNodeValue(self, index):
        if self.currentSize > index and index > 0 :
            return self.heapList[index]
        return None
        
bh=BinHeap()
bh.isEmpty()
bh.buildHeap([9,5,6,2,3,8,7,12,11,22,17,13,1,5,14,51,71,17,62,84])
#bh.buildHeap([2,2,2,2,3,3,3,3])
print(bh)

bh.insert(1)
print("kopiec po dodaniu liczby 1:")
open('C:/Users/Kom/AppData/Local/Programs/Thonny/plik.txt', 'w').write(str(bh))

print("korzeń:")
print(bh.getRoot())

print("zmiana:")
bh.editNodeValueTest(2,44)
#bh.editNodeValue(2,44)

print("wartosc 3 elementu:")
print(bh.getNodeValue(3))

print("Usuniecie korzenia:")
print(bh.delMin())
print(bh)
print(bh.delMin())
print(bh)
print(bh.delMin())
print(bh)
print(bh.delMin())
print(bh)
