# # if 1 <= N <= 1000
# # 1 <= M <= N
# # N = int(input())
# # M=12
# # print(N-M)
# # print(ord(a)-97)
# # list1=[ord(char) - 96 for char in input('Write Text: ').lower()]
# # print(list1)

# # a=[]
# # for char in input('Write Text: ').lower():
# #     a.append(ord(char) - 96)
# # print(a)

# even=[]
# odd=[]
# # for i in range(0,6):
# #     if i==0:
# #         print('zero')
# #     elif i%2==0:
# #         even.append(i)
# #     else:
# #         odd.append(i)
# # print("odd:"+str(odd))
# # print("even :"+ str(even))
# # #print(even)


# #even1 = [ i if i%2==0  else print("zero")  for i in range(1,6)  ]
# # print("odd:"+str(odd))
# #print("even :"+ str(even2))
# #print(even)









# even2 = ["even" if i%2==0  else "odd" for i in range (0,18) ] 
# print("even :"+ str(even2))

# check_alpha=["Not alpha" if not i.isalpha() else "Harsha" if i=="H" else "krishna" for i in "H/K" ]
# print(check_alpha)
string = "G1"
firstList = ["Harsha", "Krishna", "Gowtham", "Vasanth Kumar", "Raghav"]

list_comp = [[k for k in firstList] if i.isalpha() else [j for j in range(1, 6)] for i in string]

print("Using the nested comprehension in the Python along with the if /else ")
for i in list_comp:
	print(i)


check=[]
G1="A1"
F= ['Harsha', 'Krishna', 'Gowtham', 'Vasanth Kumar', 'Raghav']
for i in G1:
    if i.isalpha():
        j_add=[]
        for j in F:
            j_add.append(j)
        check.append(j_add)
    else:
        k_add=[]
        for k in range(1,6):
             k_add.append(k)
        check.append(k_add) 
for i in check:
     print(i)
#c=[for i in range(1,5) for j in F for k in G1 ]