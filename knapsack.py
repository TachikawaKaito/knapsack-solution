capacity = 45
size = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
price = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]

max_total_size = 0
max_total_price = 0

max_bag = []

n = len(size)
for i in range(2 ** n):
    total_size = 0
    total_price = 0
    bag = []
    for j in range(n):  
        if ((i >> j) & 1):
            total_size += size[j]
            total_price += price[j]
            bag.append(j + 1)
    if ((total_price >= max_total_price) & (total_size <= capacity)):
        max_total_size = total_size
        max_total_price = total_price
        max_bag = bag

print(f"容量：{max_total_size}")
print(f"値段：{max_total_price}")
print(f"組み合わせ：{max_bag}")