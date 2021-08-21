N = int(input())

an = '8'

if 1 <= N < 126:
    ans = '4'
elif 126 <= N < 212:
    ans = '6'

print(ans)
