n = int(input())
for k in range(1,n+1):
    if k == 1:
        print(0)
    elif k == 2:
        print(6)
    else:
        ncell = k*k
        total = ncell*(ncell-1)/2
        horizontal = (k-2)*(k-1)
        vertical = (k-2)*(k-1)
        print(int(total - (horizontal + vertical)*2))