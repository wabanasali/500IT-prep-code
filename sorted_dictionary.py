ls = ['james','peter','paul','james','paul','james']
#The following function takes a list and returns a dictionary of items in the list and their counts in descending order.
def sorted_asc(l):
    keys_l = [l.count(x) for x in l]
    dic = {x:y for (x,y) in zip(l, keys_l)}
    sorted_dic = dict(sorted(dic.items(),key=lambda x:x[1], reverse=True))
    return sorted_dic
    
print(sorted_asc(ls))