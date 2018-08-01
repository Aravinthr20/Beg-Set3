def median(lst):
    s = sorted(lst)
    l = len(lst)
    i = (l-1) // 2
    if (l % 2):
        return s[i]
    else:
        return (s[i] + s[i + 1])/2.0
lst=[]
n=input("Enter Number Of Input:")
for x in range(0,int(n)):
    x=input("Your Input")
    lst.append(x)
print(median(lst))
