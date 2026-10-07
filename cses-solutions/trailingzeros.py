n = int(input())
ans = 0
for i in range(1,n+1):
    ans += int(n/(5**i))
    if (5**i) > n:
        break
print(ans)