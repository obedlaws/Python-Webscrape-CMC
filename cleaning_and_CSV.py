import csv
from os import close

#Using txt files into lists and preparing it to write into CSV fils.

with open('coin_name.txt', 'r',) as a_file:
    names = []
    for line in a_file:
        stripped_names = line.strip()
        names.append(stripped_names)
        
with open('coin_symbols.txt', 'r') as b_file:
    symbols = []
    for sym in b_file:
        stripped_sym = sym.strip()
        symbols.append(stripped_sym)

with open('price_cap_volume.txt', 'r') as c_file:
    pcv = []
    for p in c_file:
        stripped_p = p.strip()
        pcv.append(stripped_p)

#Cleaning PCV into seperate lists

#Creaing Price List
length = list(range(0, 88, 3))
price = []
for p in length:
    price.append(pcv[p])

for i in range(0, len(price)):
    price[i]= float(price[i])

# Creating Marketcap List
length_2 = list(range(1, 89, 3))
marketcap = []
for m in length_2:
    marketcap.append(pcv[m])

for i in range(0, len(marketcap)):
    marketcap[i]= float(marketcap[i])

# Creating Volume List
length_3 = list(range(2, 90, 3))
volume = []
for v in length_3:
    volume.append(pcv[v])

for i in range(0, len(volume)):
    volume[i]= float(volume[i])

# Adding all lists into CSV file

def csviteration(a, b, c, d, e): 
    f = open('CMC_New_Coins.csv', 'a', newline="")
    index = 0
    writer = csv.writer(f)
    tup_ = ('coin_name', 'coin_symbol', 'price', 'marketcap', 'volume')
    writer.writerow(tup_)
    while index <= 90:
        tup = (a[index], b[index], c[index], d[index], e[index])
        writer.writerow(tup)
        if index == 90:
            break
        index += 1
    f = close()    

csviteration(names, symbols, price, marketcap, volume)

# debuggin and testing.
# print()


