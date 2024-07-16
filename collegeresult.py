import pandas as pd
def college_result():
    data=pd.read_csv('result.csv')
    college=input("Enter college name")
    d=data[data['college']==college]
    if(len(d)==0):
        print("Not found")
    else:
        print(d)