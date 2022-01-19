#find minimum number in list using recursion 
'''
def find_min(my_list):
    if(len(my_list) == 0):
        return None
    if(len(my_list) == 1):
        return my_list[0]
    temp=my_list[0] if(my_list[0]<my_list[1]) else my_list[1]
    my_list[1]=temp
    return find_min(my_list[1:])
'''

def find_min(my_list,min=None):
    if(len(my_list)==0):
        return min
    if(min == None or my_list[0]<min):
        min=my_list[0]
    return find_min(my_list[1:],min)

print(find_min([1,2,3,4,5]))
print(find_min([4,3,2,1]))
print(find_min([2,3,1,4,5]))