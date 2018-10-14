#write a python script to sort(ascending or descending) a dictionary by value.
dict1={"zara":56,"komal":23,"ritika":12}
print(dict1)
print(sorted(dict1))
print(sorted(dict1.values()))
#Wap to add key in dictionary
dict2={1:3,2:30}
print(dict2)
dict2[3]=14
print(dict2)
#wap to concatenate dictionary
d1={1:5,2:10}
d2={3:15,4:20}
d3={5:25,6:30}
d1.update(d2)
d1.update(d3)
print("concatination of dictionary is:\n",dict1)

#wap to iterate over dictionary using for loop
subjects={"chemistry":"reaction","mathematics":"logic","computer":"programming"}
for name_key, value in subjects.items():
    print(name_key,"corresponds to ", subjects[name_key])

#wap to genrate and print a dictionary that contain a number(between 1and 16)
#in the form of (x,x*x)
n=int(input("enter a number"))
d=dict()
for x in range(1,n+1):
    d[x]=x*x
    print("\n",d)
    print("-"*40)


#wap  a python script to print a dictionary where the keys are number between 1
#and 15(both included)and values are squares of keys
k=dict()
for x in range(1,15):
    d[x]=x**2
print(d)

#wap to merge two dictionaries
k1={1:10,2:20}
k2={3:30,4:40}
k1.update(k2)
print("merged dictionary is")
print(sum(k1.values()))

#wap to sum all the items in the dictionary
a1={"java":10,"php":20,"python":30}
print("sum of all the value is",sum(d1.values()))


#wap to check the given key already exist in dictionary
fruits={"banana":90,"apple":20,"mango":50}
def key(z):
    if z in fruits:
        print("key is present")
    else:
        print("key is nt present")
key("apple")
