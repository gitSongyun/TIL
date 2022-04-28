# 괄호검사

target = input()

arr = []

for i in target:

    if i == '(':
        arr.append(i)

    else:
        arr.pop(-1)

if len(arr) >= 1:
    print(arr, 'error')
else:
    print(arr, 'success')