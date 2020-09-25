# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    s=input()
    res1,res2='',''
    for l in range(len(s)):
        if l%2==0:
            res1+=s[l]
        else:
            res2+=s[l]
    print(res1,res2)