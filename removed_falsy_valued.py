#Given a list items, return a new list with all falsy values (None, 0, False, '', []) removed
def list_num(items):
    new_list=[]
    
    for i in items:
        if i:
            new_list.append(i)
    return new_list
print(list_num([True,'',0,5,"ali",False,[]]))        
        
