import math

def solve(string):
    str_list = list(string)

    if len(string) < 4:
        return string

    if len(string)%2 == 0:
        for char in string:
            if string.count(char)%2 != 0:
                return 'NO SOLUTION'            
    else:
        cont = 0
        for char in string:
            if string.count(char)%2 != 0:
                cont += 1
                mid = char
            if cont > 1:
                return 'NO SOLUTION'
                

    for j in range(len(string)//2):
        for i in range(j+1,len(string)-1):
            if str_list[j] == str_list[i]:
                str_list[i],str_list[len(string)-j-1] = str_list[len(string)-j-1],str_list[i]
                break

    if mid:
        str_list.remove(mid)
        str_list.insert(len(string)//2,mid)

    string = ''.join(str_list)
    return string

entrada = input()
print(solve(entrada))
