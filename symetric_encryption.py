message = 'secret'
cipher = 126879297332596
''' encryption '''
''' function to generate list '''
def string_to_list(msg):
    msg_list = [ord(xter) for xter in msg]
    return msg_list
    
''' function to generate integer '''
def l_to_integer(lst):
    total = 0
    lst.reverse()
    for ctr in range(len(lst)):
        total = total + lst[ctr]*(256**ctr)
    return total

''' decryption '''
def expand(n,b):
    lst = []
    q = n
    while q != 0:
        lst.append(q%b)
        q = q//b
    lst.reverse()
    return lst

def l_to_str(lst):
    msg = ''
    for nbr in lst:
        msg = msg + chr(nbr)
    return msg
    
print(l_to_integer(string_to_list(message)))

print(l_to_str(expand(cipher,256)))
