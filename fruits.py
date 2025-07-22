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
        


numbers = [70, 80, 65, 90, 100]
numm=len(numbers)
print(numm)
total=0
for nuu in numbers:
    total+=nuu
pp=total/numm
print(pp)

word = "python"

for w in word:
    print(w)

for r in range(1,10):
    for t in range(1,10):
        y=r*t
        print(y)
        
        

pulse_rate=[55,43,78,38,96,51]
#print(pulse_rate[0])
print(pulse_rate.index(55))
for i in range(len(pulse_rate)):
    print(f"{i+1}番目の猫の脈拍は{pulse_rate[i]}です")
        
max_pulse = max(pulse_rate)
min_pulse= min(pulse_rate)
max_index = pulse_rate.index(max_pulse)
min_index=pulse_rate.index(min_pulse)
print(f"一番脈拍が高いのは{max_index+1}番目の{max_pulse}です")
print(f"一番脈拍が低いのは{min_index+1}番目の{min_pulse}です")
total=[]
for ii in pulse_rate:
    if ii>=60:
        #print(ii)
        oo=pulse_rate.index(ii)
        print(f"{oo+1}番目の猫({ii})")
        total.append(ii)
        #print(total)
        uu=len(total)
        #print(uu)
print(f"60以上の猫は{uu}匹です")
count=0
for inu in pulse_rate:
    count+=inu
print(count)
bb=len(pulse_rate)
cc=count/bb
cc=round(cc, 1)
print(cc)

fruits = {
    "apple": 5,
    "banana": 2,
    "orange": 0,
    "grape": 7
}

for a,b in fruits.items():
    if b>0:
        print(a,":",b)

