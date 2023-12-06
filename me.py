import functools
x= input("Enter the nunber : ")
def numbers(x):
    i = 0
    result_list = []
    while i <int(x):
        i = i+1
        result_list.append(i)
    return result_list

try:
    n = functools.reduce(lambda x,y : x*y ,numbers(x))
except ValueError as e :
   print("Enter numbers only!")
else:
   print(int(x),"! = ",n) 