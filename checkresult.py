import pandas as pd
def check_result():
    data=pd.read_csv('result.csv')
    rollno=int(input("Enter roll number"))
    d=data[data['roll']==rollno]
    if(len(d)==0):
        print("Roll not found")
    else:
        print(d)