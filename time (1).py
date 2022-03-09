def 1 time(h,m,s):
    time=(self,h,m,s)
    self.h1=h
    self.m1=m
    self.s1=s
def add(sum,x):
    sum=(self,sum1,sum2,sum3)
    self.sum1=self.h1+self.x
    self.sum2=self.m1+self.x
    self.sum3=self.s1+self.x
sum3=0
sum2=0
sum1=0
if sum3<=60:
 sum3=sum3-60
 sum3=sum2+sum3
sum2=0
if sum2<=60:
 sum2=sum2-60
 sum2=sum2+sum1
print("enter the time1")
h1=(input("enter the h1"))
m1=(input("enter the m1"))
s1=(input("enter the s1"))
print("enter the time2")
h2=(input("enter the h2"))
m2=(input("enter the m2"))
s2=(input("enter the s2"))
sum=0
sum1=h1+h2
print("sum1",h1, "+" ,h2)
sum2=0
sum2=m1+m2
print("sum2",m1, "+" ,m2)
sum3=0
sum3=s1+s2;
print("sum3",s1, "+" ,s2)
st=sum1+sum2+sum3
print("sum of two time",st)










