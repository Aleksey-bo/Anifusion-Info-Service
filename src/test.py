a = [1, 2]
b = [3, 2, 4]


for item in b:
    try:
        if len(a) > b.index(item):
            print(a[b.index(item)])
    except Exception:
        print("Error")
