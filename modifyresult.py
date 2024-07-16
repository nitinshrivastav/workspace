import pandas as pd
from login import login
def modify_result():
    ans=login()
    if(ans==1):
        data=pd.read_csv('result.csv')
        rollno=int(input("Enter your rollnumber"))
        print('press 1 for name change')
        print('press 2 for maths change')
        print('press 3 for science change')
        print('press 4 for english change')
        choice=input("Enter your choice")
        rolldata=list(data['roll'])
        if(rollno in rolldata):
            ind=rolldata.index(rollno)
            if(choice=='1'):
                name=input("Enter your new name")
                data['name'][ind]=name
                print("Name has been changed")
            elif(choice=='2'):
                maths=input("Enter your new maths marks")
                data['math'][ind]=maths
                print("Marks has been updated")
            elif(choice=='3'):
                science=input("Enter your new science marks")
                data['sci'][ind]=science
                print("Marks has been updated")
            elif(choice=='4'):
                eng=input("Enter your new english marks")
                data['eng'][ind]=eng
                print("Marks has been updated")
            else:
                print('Wrong choice')
            data.to_csv('result.csv',index=False)
        else:
            print("Roll number is not correct")