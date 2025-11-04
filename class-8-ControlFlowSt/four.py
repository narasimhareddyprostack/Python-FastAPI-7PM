enames=["RG","SG","PG","NM"]
eids=(101,102,103,104,105)
uids={101,101,102,103}
ename="Rahul"
b = bytes([10,20,30,255])
ba =bytearray([10,20,30,255])
fz=frozenset({10,10,20,10})   #duplicate not allowed
#numbers=range(10)
numbers=range(0,10,1)

for ch in ename:
    print(ch)

""" 
for element in fz:
    print(element)
 """
""" for num in numbers:
    print(num) """

""" 
for ename in enames:
    print(ename) """
