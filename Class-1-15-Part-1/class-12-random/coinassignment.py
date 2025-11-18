from random import choice
coin=['Head','Tail']

head_count=0
tail_count=0

for value in range(1,101):
    result=choice(coin)
    if result =="Head":
        head_count=head_count+1 
    elif result=="Tail":
        tail_count=tail_count+1

print("Tail Count:",tail_count)
print("Head Count:",head_count)