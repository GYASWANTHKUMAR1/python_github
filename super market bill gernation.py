from datetime import datetime

name=input("Enter the Name:")
#lists of items
Lists='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
salt    Rs 20/kg
Oil     Rs 80/kg
Paneer  Rs 110/kg
Maggie  Rs 50/kg
Boost   Rs 90/kg
Colgate Rs 85/Kg
'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]
 
#rates for items
items={'rice':20, 'sugar':30,'salt':20,
'oil':80,'paneer':110,
'maggi':50,'boost':90,'colgate':85}

option=int(input("for list of items press 1:"))
if option==1:
    print(Lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*items[item]

            pricelist.append(( item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("Sorry you entered item is not available")
    else:
        print("You entered wrong number")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=",'Vijay supermarket',25*'=')
            print(28*" ", "wanaparthy")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",10*" ",'items',8*" ",'quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,12*' ',ilist[i],10*' ',qlist[i],10*" ",plist[i])
            print(75*"-")
            print(50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"-")
            print(50*" ",'finalamount:','Rs',finalamount)
            print(75*"-")
            print(25*"-",'Thanks for visiting',25*"-")
            print(75*"-")
