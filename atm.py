
class Bank:
    def __init__(self,bank_name,branch,account_no,cvv,otp):
        self.name=bank_name
        self.branch_bank=branch
        self.account_nol=account_no
        self.cvvv=cvv
        self.onetp=otp
    def check_b(self):
        print("balance is 💲 100000000000000")    
    def withdraw(self,amount):
        newbalance=100000000000000-amount
        print("you have withdrawn ",amount,"\n your remaining balance is ",newbalance)    

def main():
    bank=input("Enter your bank name : ")
    branch1=input("enter the branch : ")
    accn=input("Enter the account number : ")
    cvv=input("Enter the cvv : ")
    ottp=input("Enter the otp: ")
    user1=Bank(bank,branch1,accn,cvv,ottp)
    print("choose your activity")
    print("1. balance enquiry 2. withdraw")
    option=int(input("Enter your opetion in number"))
    if option==1:
        user1.check_b()
    elif option==2:
        amount=int(input("enter the amount"))
        user1.withdraw(amount)
    else:
        print("Enter 1 or 2")
main()