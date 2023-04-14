n = int(input())
a = list(map(int, input().split()))
x = int(input())

closest = a[0]  

for i in range(1, n):
    if abs(a[i] - x) < abs(closest - x):  
        closest = a[i]  

print(closest)