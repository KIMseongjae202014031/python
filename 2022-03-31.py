price_list = [32100, 32150, 32000, 32500]      
for i in range(len(price_list)):
        print(i, price_list[i])  

k=0
price_list = [32100, 32150, 32000, 32500]      
for i in range(100,130,10):
  k += 1
print(i, price_list[k])

for i in range(2002,2054,4):       
   print(i)

for i in range(10):        
   print(i/10)

ricker = "btc_krw"
ricker = ricker.upper()
print(ricker)
        

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

a= "hello world"
print(a.split())

data = "2020-05-01"
print(data.split("-"))

samsung = '5,969,782,550'
samsung = samsung.replace(',','')
int(samsung)
print(samsung)

a= "hello world"
print(a.split())

price = ['20180728',100,130,140,150,160,170]
print(price[1:6])

num = [1,2,3,4,5,6,7,8,9,10]
print(num[1::2])

list = [3,100,23,44]
for i in range(4):
   if list[i] %3 == 0:
       print(list[i])
