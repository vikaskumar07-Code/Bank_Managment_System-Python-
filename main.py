
import json
import string
import random
from pathlib import Path



class Bank:
    database = 'bank_managment_system/data.json'
    data= []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"The error is occured as {err}")
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
    
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info={
            "name":input("Tell your name :- "),
            "age":int(input("Tell your Age :- ")),
            "email": input("Tell your Email Address :- "),
            "Pin": input("Tell your 4 Pin :- "),
            "accountNo.": Bank.__accountgenerate(),
            "Balance": 0
        }

        if info['age'] < 18 or len(str(info['Pin'])) != 4:
            print("Sorry you can't create a account ")
        else:
            print("account has been created Successfully !!")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please note down your account number")
            Bank.data.append(info)

            Bank.__update()
    
    def depositmoney(self):
        accnumber = input( "Please tell your account number :- ")
        Pin = int(input("Please tell your Pin code :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber or i['Pin']== Pin]

        if userdata == False:
            print("Sorry we can't access your account !! Try again later.")
        else:
            amount = int(input("How much amount you want to deposit :- "))
            if amount > 10000 or amount < 0:
                print("Sorry this amount is too much you can deposit below 10,000 and above 0")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount deposited Succesfully !! ")

    def withdrawnmoney(self):
        accnumber = input( "Please tell your account number :- ")
        Pin = int(input("Please tell your Pin code :- "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber or i['Pin']== Pin]

        if userdata == False:
            print("Sorry we can't access your account !! Try again later.")
        else:
            amount = int(input("How much amount you want to withdraw :- "))
            if userdata[0]['Balance'] < amount:
                print("Sorry you have the Insufficent Balance !! Try again Later")

            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Amount Withdarawn Succesfully !! ")

    def showdetails(self):
        accnumber = input( "Please tell your account number :- ")
        Pin = int(input("Please tell your Pin code :- "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber or i['Pin']== Pin]
        print( "Your Information are here :- \n\n")
        for i in userdata[0]:
            print(f"{i}: {userdata[0][i]}")
        

    def updatedetails(self):
        accnumber = input( "Please tell your account number :- ")
        Pin = int(input("Please tell your Pin code :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber or i['Pin']== Pin]

        if userdata == False:
            print("no such user found ")
        else:
            print("Disclaimer :- You don't have access to change Age , Account No. , Balance ")

            print("Fill the details for change or leave it empty for no change")

            newdata={
                "name" : input("Tell new user name :-"),
                "email" : input("Tell your new email or press enter to Skip:- "),
                "Pin" : input("Enter new Pin or press enter to skip :- ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["Pin"] == "":
                newdata["Pin"] = userdata[0]['Pin']
            
            newdata['age'] = userdata[0] ['age']

            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['Balance'] = userdata[0]['Balance']

            if type(newdata['Pin']) == str:
                newdata['Pin'] = int(newdata['Pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i] 
            
            Bank.__update()
            print("Details Was Updated Succesfully !!")

    def Delete(self):
        accnumber = input( "Please tell your account number :- ")
        Pin = int(input("Please tell your Pin code :- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber or i['Pin']== Pin]

        if userdata ==False:
            print("Sorry no such Data found !! Try again later ")
        else:
            check = input("Press Y for delete account OR N for escape :- ")
            if check == 'N'or check == 'n':
                pass
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Accont Deleted Successfully !!")
                Bank.__update()
            




user=Bank()
print("Intrustion's\n")
print("Press 1 for Creating an account")
print("Press 2 for Deposit money in the bank ")
print("Press 3 for WithDrawn the Money ")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for delete your account")

check = int(input("Response :- "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawnmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()