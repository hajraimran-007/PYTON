#Given a list of keys and a default value, return a dictionary where each key maps to the default value.
def list_values(keys):
    default=0
    default_dic={}
    for i in keys:
        default_dic[i]=default
    return default_dic
print(list_values(["sara","ali","ahmed"]))