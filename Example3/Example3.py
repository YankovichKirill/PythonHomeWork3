lst = list(map(float, input("Enter numbers separated by spaces:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]
print(max(new_lst) - min(new_lst))