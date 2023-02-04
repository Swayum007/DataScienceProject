import time
print(".........   Welcome to SBI QUERY PORTAL  ........")
print("  ")
print("For any queries please check the below questions :- ")
print("  ")
ch='Yes'
while ch=='Yes' or ch=='yes': 
        print("        Please Choice any number from 1 to 10 to select the  questions      "),
        print("----------------------------------------------------------------------------"),
        print("  "),
        print("1.What is the process of applying for an SBI Card? ?"),
        print("2.How to open a Bank Account ?"),
        print("3.Do I need to pay some amount to open my bank Account ?"),
        print("4.What are bank fees ?"),
        print("5.Is there a minimum balance required ?"),
        print("6.Does the bank have good customer service ?"),
        print("7.Does the bank have online banking and a mobile app ?"),
        print("8.Can your money be insured ?"),
        print("9.Does our bank give different types of loans ?"),
        print("10.What are the benefits to open an account in your bank ?"),
        print("-----------------------------------------------------------------"),
        print("  "),
        a = input()
        if a==1 :
            print("The fastest way to apply for an SBI Card is through our website www.sbicard.com"),
            print("Alternatively, you can also call SBI Card helpline at 39 02 02 02 (please prefix the STD Code of your city) or visit the nearest SBI branch to apply for an SBI Card."),
        elif (a==2):
            print('''A valid, government-issued photo ID, such as a driver’s license or a passport.
                Nondrivers can get a state ID card at the Department of Motor Vehicles office.''');
            print("Other basic information, such as your birthdate, Social Security number or Taxpayer Identification Number, or phone number."),
            print('''Identification details for other applicants, if you are opening a joint account: 
                Because the account will be owned by multiple people, the bank will want all owners
                identification and personal information.'''),
            print("A co-owner if you are not yet 18. Ask a parent or legal guardian to sign legal documents with the bank."),
        elif a==3 :
            print("No, There is no need to pay any amount to open a bank account in our bank.")
        elif a==4 :
            print('''The term bank fees refers to any charges imposed by financial institutions
                on their personal and business customers for account set-up, maintenance, and minor transactional services.
                These fees may be charged on a one-time or ongoing basis.''')
        elif a==5 :
            print("NO, SBI provides a good feature that anyone can have an acconut without any minimum balance")
        elif a==6 :
            print('''Yes, SBI gives first priority to our customers,
                    So that they should not face any difficulties''')
        elif a==7 :
            print('''Yes,We have online banking features too 
                    And apps like :-
                    YONO SBI : Banking & LIfestyle
                    YONO Lite SBI - Mobile Banking
                    SBI Card
                    ..and many more''')
        elif a==8 :
            print('''       All the deposits of our customers are insured under 
                the Deposit Insurance and Credit Guarantee Corporation of India scheme.''')
        elif a==9 :
            print('''Yes, SBI provides you with the different type of loans i.e -
                    Home Loan
                    Study Loan
                    Personal Loan
                    Loan against Property
                    ..etc''')
        elif a==10 :
            print('''SBI has removed the minimum requirement of ₹1000 in account to nil, 
                    so you'll not be fined anything even if you have least balance in your account.
                    SBI internet banking is free too. You won't be charged anything for that too. 
                    Plus there are no charges for SMS alerts.''')
        else :
            print("Sorry The enterd choice is not mentioned in the above questions")
            print("   ")
            print('   ') 
            time.sleep(2)   
            ch=input('''Do you want to continue 
                     Yes/No  
                     ''')           
print("   ")
print('   ')
print("Thanks to visit our SBI Query Portal")
