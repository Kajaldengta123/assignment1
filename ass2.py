#list
#Q.1- Create a list with user defined inputs
lst=list(input().split())
print(lst)

#Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
lst2=lst+['google','apple','facebook','microsoft','tesla']
print(lst2) 

#Q.3 - Count the number of time an object occurs in a list.
print(lst2.count('tesla'))

#Q.4 - create a list with numbers and sort it in ascending order.
lst1=[12,45,32,87,90,2,13]
lst1.sort()
print(lst1)
#Q.5 Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
a=[23,45,67,89,65]
b=[12,54,23,98,10]
c=a+b
c.sort()
print(c)

#Q.6 - Count even and odd numbers in that list.
lst3=[1,65,34,7,9,12]
no_even=0
no_odd=0
for i in lst3:
    if i%2==0:
        no_even +=1
    else:
        no_odd +=1
print('count of even numbers'+str(no_even))
print('count of odd numbers'+str(no_odd))

#tuples
#Q.1-Print a tuple in reverse order.
tup1=(12,5,6,9,8)
print(tup1[::-1])

#Q.2-Find largest and smallest elements of a tuples.
tup2=(12,13,90,67,35,2)
print('largest:',max(tup2),"smallest",min(tup2))

#Strings
#Q.1- Convert a string to uppercase.
x="hello everyone"
x=x.upper()
print(x)

#Q.2- Print true if the string contains all numeric characters.
y="78927"
print(y.isnumeric())

#Q.3- Replace the word "World" with your name in the string "Hello World".
z="hello world"
z=z.replace("world","kajal")
print(z)



