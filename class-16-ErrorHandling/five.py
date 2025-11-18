try:
    a=int(input("Enter First No:"))
    b=int(input("Enter Second No:"))
    print(a/b)

except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
    
print("GE")