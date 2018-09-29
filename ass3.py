#Q.1- Reverse the whole list using list methods.
lst=[10,20,30,'python','perl','c',12]
lst.reverse()
print(lst)
#Q.2- Print all the uppercase letters from a string.
s="My Name is Kajal"
for i in s:
    if i==i.upper():
        print(i,end="|")
#Q.3- Split the user input on comma's and store the values in a list as integers.
lst3=list(map(int,input("enter the elements").split(",")))
lst4=list(input("enter the elements").split(","))
print(*lst3)
print(*lst4)

#Q.4- Check whether a string is palindromic or not.
a="carrac"
if a[::-1]==a:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
#shallo copy
x5=[11,22,33]
x6=x5
print("original list:",x5,"id=",id(x5))
print("shallow copylist:",x6,"id=",id(x6))
#deep copy
x7=x5.copy()
print("original list",x5,"id=",id(x5))
print("deep copy list",x7,"id=",id(x7))
