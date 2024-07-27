import csv
import os
print("السلام علیکم ورحمتہ اللہ وبرکاتہ.\nWelcome to simple Bank Account")

def Bank_account_Exsist():                                                
    if os.path.exists(f"{File_name}.csv"):
            print("Your account exsist")
            Balance= input("Enter Your balance: ")
            with open (f"{File_name}.csv","a",newline='') as f:
                    writing = csv.writer(f)
                    writing.writerow([f"Your balance is {Balance}\n"])
            print("Your transition successfully Completed.\nThank You!")
def Bank_account_Not_Exsist():
            
                if  os.path.exists(f"{File_name}"):
                    print("Your account is exsist ")
                elif(print):
                    print("Your account is not exsist do you want create new one?."
                    "Then press 'ENTER'; ")
                enter = input("'Press Enter':  ")
                print(enter)
                
                New_Account_Name=input("Enter your new account name: ")
                with open(f"{New_Account_Name}.csv","w",newline="") as f:
                    f.close()
                print("Your account Has been created successfully")
                Balance= input("Enter Your balance: ")         
                with open (f"{New_Account_Name}.csv","a",newline="") as f:
                    writing = csv.writer(f)
                    writing.writerow([f"Your balance is {Balance} \n"])
                print("Your transition successfully Completed.\nThank You!")
File_name=input("Enter your File name: ")
if os.path.exists(f"{File_name}.csv"):
       Bank_account_Exsist()
else:
      Bank_account_Not_Exsist()
