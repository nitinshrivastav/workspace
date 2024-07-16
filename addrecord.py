import pandas as pd
from login import login
def add_record():
    status=login()
    if(status==1):
        data=pd.read_csv('result.csv')
        roll=int(input('Enter your roll number'))
        name=input('Enter your name')
        college=input('Enter college nam')
        m=int(input('Enter marks in maths'))
        s=int(input('Enter marks in science'))
        e=int(input('Enter marks in english'))
        rolldata=list(data['roll'])
        if(roll in rolldata):
            print('Roll already exist')
        else:
            d={'name':[name],'roll':[roll],'college':[college],'math':[m],'eng':[e],'sci':[s]}
            df=pd.DataFrame(d)
            data=pd.concat([data,df],axis=0)
            data.to_csv('result.csv',index=False)
            print("Record has been added")