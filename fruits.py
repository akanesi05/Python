fruits = ["apple", "banana", "orange"]

for f in fruits:
    print(f)


for n in range(1,11):
    n+=n
    print(n)
    

for num in range(21):
    if num%2==0:
        print(num)


items = {
    "pen": 120,
    "notebook": 300,
    "eraser": 80
}

for it,itt in items.items():
    print(f"{it}は{itt}円")

scores = {
    "Taro": 75,
    "Hanako": 85,
    "Ken": 90,
    "Yuki": 65
}

for sc,scc in scores.items():
    if scc>=80:
        print(f"80点以上は{sc}")
        

