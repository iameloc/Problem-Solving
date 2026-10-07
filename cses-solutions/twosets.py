n = int(input())
seq = []
seq1 = []
seq2 = []
for i in range(1,n+1):
    seq.append(i)


if n<3:
    print('NO')

elif n == 3:
    seq1 = [1,2]
    seq2 = [3]
    print('YES')
    print(2)
    for i in range(len(seq1)):
        if i == len(seq1)-1:
            print(seq1[i])
        else:
            print(seq1[i], end=' ')
    print(len(seq2))
    for i in range(len(seq2)):
        if i == len(seq2)-1:
            print(seq2[i])
        else:
            print(seq2[i], end=' ')

elif n == 7:
    seq1 = [1,2,5,6]
    seq2 = [3,4,7]
    print('YES')
    print(len(seq1))
    for i in range(len(seq1)):
        if i == len(seq1)-1:
            print(seq1[i])
        else:
            print(seq1[i], end=' ')
    print(len(seq2))
    for i in range(len(seq2)):
        if i == len(seq2)-1:
            print(seq2[i])
        else:
            print(seq2[i], end=' ')
    
elif (n-3)%4 == 0 and n>3:
    seq1 = [1,2]
    seq2 = [3]
    for i in range(4,n,4):
        seq1.append(i)
        seq2.append(i+1)
        seq2.append(i+2)
        seq1.append(i+3)
    print('YES')
    print(len(seq1))
    for i in range(len(seq1)):
        if i == len(seq1)-1:
            print(seq1[i])
        else:
            print(seq1[i], end=' ')
    print(len(seq2))
    for i in range(len(seq2)):
        if i == len(seq2)-1:
            print(seq2[i])
        else:
            print(seq2[i], end=' ')

elif n%4 == 0 and n>3:
    for i in range(1,n+1,4):
        seq1.append(i)
        seq2.append(i+1)
        seq2.append(i+2)
        seq1.append(i+3)
    print('YES')
    print(len(seq1))
    for i in range(len(seq1)):
        if i == len(seq1)-1:
            print(seq1[i])
        else:
            print(seq1[i], end=' ')
    print(len(seq2))
    for i in range(len(seq2)):
        if i == len(seq2)-1:
            print(seq2[i])
        else:
            print(seq2[i], end=' ')

else:
    print('NO')
    

'''
que codigo feio
para olhar o lado positivo, fiz sem auxilio nenhum =)
'''