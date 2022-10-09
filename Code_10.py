
lst_0=[]
lst_1=[]
lst_2=[]
lst_3=[]
str_0=input("").split(" ")
lst_0.append(str_0)

while ['STOP'] not in lst_0:
    str_0 = input("").split(" ")
    lst_0.append(str_0)


for i in lst_0[:-1]:
    lst_1.append(i)


for j in lst_1:
    for k in j:
        lst_2.append(int(k))
    lst_3.append(lst_2)
    lst_2=[]

flag=False
abs_0=0
lst_5=[]
lst_6=[]
lst_7=[]
for i in lst_3:
    for j in range(0,len(i)-1):
        if i[j+1]>i[j]:
            lst_5.append(i[j+1]-i[j])
        else:
            lst_5.append(i[j]-i[j+1])
    lst_6.append(lst_5)
    lst_5=[]


for l in lst_6:
    for p in range(1,len(l)+1):
        if p in l:
            flag=True
        else:
            flag=False
    if flag:
        lst_7.append("UB Jumper")
    else:
        lst_7.append("Not UB Jumper")


for t in lst_7:
    print(t)

str_0=input("")
low_0=""
upp_0=""
odd_0=""
even_0=""

for i in str_0:
    if  i.islower():
        low_0+=i
    elif i.isupper():
        upp_0+=i
    elif i.isdigit():
         if int(i)%2==0:
            even_0+=i
         else:
             odd_0+=i


def sort_my_str(x):
    str_01=""
    x=sorted(x)
    for i in x:
        str_01+=i
    return str_01


low_0=sort_my_str(low_0)
upp_0=sort_my_str(upp_0)
odd_0=sort_my_str(odd_0)
even_0=sort_my_str(even_0)

final_str=low_0+upp_0+odd_0+even_0

print(final_str)

