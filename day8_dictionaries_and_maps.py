# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
my_dict={}
for i in range(n):
    key,val= list(map(str,input().split()))
    my_dict[key]=val

try:
    while True:
        q=input()
        if q in my_dict:
            print("{}={}".format(q,my_dict[q]))
        else:
            print("Not found")
except:
    pass