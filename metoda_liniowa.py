class EmptyCell: pass

class UsedCell: pass

def get_hash_value(object):
    return abs(hash(object))%10

counter = 0

def add_elements_to_line(tab_elements, line_tab):
    new_loop_holder = 0
    for i in range(len(tab_elements)):
        element = tab_elements[i]
        position = get_hash_value(element)
        for i in range(position,len(line_tab),1):
            if line_tab[i] == EmptyCell or line_tab[i] == UsedCell:
                line_tab[i] = element
                break
            if i == len(line_tab) - 1:
                new_loop_holder = 1
        if new_loop_holder == 1:
            for i in range(0,position,1):
                if line_tab[i] == EmptyCell or line_tab[i] == UsedCell:
                    line_tab[i] = element
                    break
                if i == position:
                    return 1

def add_one_element(elem, line_tab):
    new_loop_holder = 0
    element = elem
    position = get_hash_value(element)
    for i in range(position,len(line_tab),1):
        if line_tab[i] == EmptyCell or line_tab[i] == UsedCell:
            line_tab[i] = element
            break
        if i == len(line_tab) - 1:
            new_loop_holder = 1
    if new_loop_holder == 1:
        for i in range(0,position,1):
            if line_tab[i] == EmptyCell or line_tab[i] == UsedCell:
                line_tab[i] = element
                break
    if check_if_more_than_60(line_tab) >= 0.6:
        new_line_tab = [len(line_tab)*2]
        fill_start_line_table(new_line_tab)
        add_elements_to_line(rehash_line_table, new_line_tab)
        line_tab = new_line_tab
        

def check_if_more_than_60(line_tab):
    count_elements = 0
    for i in range(len(line_tab)):
        if line_tab[i] != EmptyCell and line_tab[i] != UsedCell:
            count_elements+=1
    return count_elements/len(line_tab)

def rehash_line_table(line_table):
    iterator = 0
    tmp_tab = []
    for i in len(line_table):
        if line_table[i] != EmptyCell and line_table[i] != UsedCell:
            tmp_tab.append(line_table[i])
            iterator += 1
    return tmp_tab
    

def fill_start_line_table(number_of_elements):
    line_tab = []
    for i in range(0,number_of_elements,1):
        line_tab.insert(i, EmptyCell)
    return line_tab

def find_in_line_table(element, line_tab):
    global counter
    counter = 0
    k = get_hash_value(element)
    for i in range(k, len(line_tab)):
        if line_tab[i] != element or line_tab[i] == UsedCell:
            counter+=1
        elif line_tab[i] == element or line_tab[i] == EmptyCell:
            counter+=1
            return i
            break
        if i == len(line_tab) - 1:
            for j in range(0,get_hash_value(element),1):
                if line_tab[j] != element or line_tab[j] == UsedCell:
                    counter+=1
                elif line_tab[j] == element or line_tab[j] == EmptyCell:
                    counter+=1
                    return j
                    break          
    

def delete_from_line_table(object, line_tab):
    index = find_in_line_table(object, line_tab)
    line_tab[index] = UsedCell

        
def find_in_chain_table(object, chain_tab):
    global counter
    counter = 0
    hash_code = get_hash_value(object)
    for v in chain_tab[hash_code]:
        counter+=1
        if v == object:
            return True, hash_code
    return False, hash_code

def prepare_for_chain_table(n):
    return [[] for _ in range(n)]

def insert_one_into_chain_table(object, chain_tab):
    chain_tab[get_hash_value(object)].append(object)
    
def insert_table_into_chain_table(chain_tab, elements_tab):
    for i in range(len(elements_tab)):
        chain_tab[get_hash_value(elements_tab[i])].append(elements_tab[i])

def delete_from_chain_table(object, chain_tab):
    hash_code = find_in_chain_table(object)
    if hash_code[0]:
        chain_tab[hash_code[1]].remove(object)
            


elements = 10,15,16,25,14,24,29,28,12,35
line_tabb = fill_start_line_table(20)
add_elements_to_line(elements, line_tabb)
add_one_element("a", line_tabb)
find_in_line_table("a", line_tabb)
print(counter)
print(line_tabb)


chain_tab = prepare_for_chain_table(20)
# insert_into_chain_table(10, chain_tab)
insert_table_into_chain_table(chain_tab, elements)
print(find_in_chain_table(25, chain_tab))
print(counter)


