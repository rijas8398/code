arr = [2, 4, 5, 0, 2, 7, 0, 0]
n = len(arr)
cnt = 0
x = 0

cnt = 0
for i in range(len(arr)):
    if arr[i] == x:
        continue

    else:

        arr[cnt] = arr[i]
        cnt += 1

while cnt < len(arr):
    arr[cnt] = x
    cnt += 1

print(arr)