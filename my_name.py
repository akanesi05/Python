my_name="aa"
favorite_language="Python"

print(f"私の名前は{my_name}です。年齢は25歳で、好きなプログラミング言語は{favorite_language}です。")

aa=1200
bb=800

cc=aa+bb
print(cc)

dd=(cc/10)
print(dd)

#交換前: a = 10, b = 20
#交換後: a = 20, b = 10

# a=10
# b=20
# print(a,b)
# b=a
# tmp=b
# a=tmp
# print(a,b)


a = 10
b = 20
print(f"交換前: a = {a}, b = {b}")

# 正しい値交換の手順
tmp = a    # 1. aの値を一時保存
a = b      # 2. bの値をaに代入
b = tmp    # 3. 一時保存したaの値をbに代入

print(f"交換後: a = {a}, b = {b}")
