def solve(string):
    freq = {}
    for char in string:
        freq[char] = freq.get(char,0)+1

    odd = [char for char in freq if freq[char]%2 != 0]

    if len(string)%2 == 0 and odd:
        return 'NO SOLUTION'
    if len(string)%2 != 0 and len(odd) != 1:
        return 'NO SOLUTION'

    mid = odd[0] if odd else ''

    esq = ''
    for char in freq:
        esq += char*(freq[char]//2)

    return esq + mid + esq[::-1]

entrada = input()
print(solve(entrada))