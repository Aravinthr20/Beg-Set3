h=input("Hour1:")
m=int(input("Minute1:"))
h1=input("Hour2:")
m1=int(input("Minute2:"))
ho=int(h)*60+m
ho1=int(h1)*60+m1
v=[ho,ho1]
v.sort()
z=max(v)-min(v)
min=int(z)%60
hou=int(z)/60
print(int(hou),":",min)