scores = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eve": 78
}

for n,m in scores.items():
    if m >=80:
        print(n)
        


fruits = {
    "apple": 5,
    "banana": 2,
    "orange": 0,
    "grape": 7
}

for a,b in fruits.items():
    if b>0:
        print(a,":",b)


work_hours = {
    "Taro": 45,
    "Hanako": 38,
    "Ken": 50,
    "Yuki": 42
}


for c,d in work_hours.items():
    if d>=40:
       print(f"{c}は{d-40}時間残業してます")

stock = {
    "pen": 10,
    "notebook": 0,
    "eraser": 3,
    "pencil": 0,
    "ruler": 5
}

out_of_stock=[]
for e,f in stock.items():
    if f==0:
        out_of_stock.append(e)
print(out_of_stock)



cart = {
    "apple": {"price": 100, "quantity": 3},
    "banana": {"price": 80, "quantity": 0},
    "orange": {"price": 120, "quantity": 2}
}


list=0
for g,h in cart.items():
    if h["quantity"]>=1:
        list+=h["price"]
        print(g)
        
print(f"合計金額: {list}円")    
        
        
results = {
    "Alice": [85, 90, 78],
    "Bob": [72, 60, 68],
    "Charlie": [90, 95, 92],
    "David": [65, 70, 58]
}


#print(results["Alice"])

for num,mum in results.items():
    s=sum(mum)/len(mum)
    #print(s)
    if s>=80:
       print(f"{num}:{s}")
    