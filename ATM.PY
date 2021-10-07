# #ATM CODE
# print("welcome to Bank OF India")
# print("please insert your card")
#     language=input("enter your language:")
#     if language=="english" or "hindi":
#         print(language)
#         pin=int(input("enter your pin:"))
#         if pin== 1234 :
#             print(pin,"pin has been matched")
#             trans=input("enter your transaction:")
#             if trans =="cash withdrawn":
#                 print(trans,"withdraw")
#                 type=input("enter your account type:")
#                 if type=="current account"  or  "saving account":
#                     print(type,"current account")
#                     account_ammount=int(input("enter check your account ammount: "))
#                     if account_ammount <= 50000:
#                         print("withdrawal maoney")
#                         ammount=int(input("enter your ammount:"))
#                         if ammount== 24000 :
#                          print(ammount)
#                          transaction=input("your transaction is successful:")
#                          if transaction== "yes"or "no":
#                              print(transaction)
#                              receipt=input("do you want recipt:")
#                              if receipt== "yes"  or "no":
#                                  print(receipt)
#                              else:
#                                  print("no receipt")
#                          else:
#                              print(" transaction unsuccessful")
#                         else:
#                             print("no ammount")
#                     else:
#                         print("zero account blance")
#                 else:
#                     print("no any account type")
#             else:
#                 print("transaction failed")
#         else:
#             print("not")
#     else:
#         print("not language")
# else:
#     print("not verified card")    



















# print("Welcome to State bank of India")
# p=int(input("Enter your 4 digit pin number:"))
# m=25000
# if(p==1234):
#     print("1.withdraw")
#     print("2.Fast Cash")
#     c=int(input("please choose transactions:"))
#     if(c==1):
#         w=int(input("enter withdraw amount:"))
#         if(w<m and w%100==0):
#             print("please take your amount:",w)
#         else:
#             print("invalid cash")
#     elif(c==2):
#         print("your available amount:",m)
#     elif(c==3):
#         print("1->5000")
#         print("2->10000")
#         print("3->15000")
#         print("4->20000")
#         f=int(input("Enter the fast cash option:"))
#         if(f==1 and 5000<m):
#             print("please take cash 5000")
#         elif(f==2 and 10000<m):
#             print("please take cash 10000")
#         elif(f==3 and 15000<m):
#             print("f==3 and 15000<m")
#         elif(f==4 and 20000<m):
#             print("f==4 and 20000<m")
#         else:
#             print("invalid fast cash option")
#     else:
#         print("wrong choice")
# else:
#     print("wrong pin number")
        



        #OR


print("welcome  to state bank of india")
print("please insert your card")
pin_inp =1234
pin = int(input("please enter your pin:"))
if pin==1234:
    print("1.blance enquiry")
    print("2.withdraw money")
    print("3.deposite money")
    print("4.transfer money")
    print("5.quit")
    transaction = input("which mode you prefer(please select the no)")
    if transaction=="1":
        slip=input("do you want to slip")
        if slip=="yes":
            print("collect your slip")
        else:
            print("thank you for visiting us")
    elif transaction=="2":
        amount=int(input("enter your amount for withdraw amount"))
        if amount<=100000:
            #print("please collect cash")
            #if transaction-amount
            print(100000-amount,"this is your bank balance")
        else:
            print("please enter valid ammount for withdraw")
    elif transaction=="3":
        deposite=int("enter ammount which you want to deposite")
        if deposite>0:
             print("your money is successfully deposite")
        else:
            print("please enter valid ammount for deposite your money")
    elif transaction=="4":
        trans=int(input("transfer money is"))
        if trans>0:
             print("your money is successfully transfer")
        else:
            print("please enter valid ammount for transfer")
    elif transaction=="5":
        print("quit")
    else:
          print("please choose any tranjaction")
else:
        print("please enter valid pin.....")