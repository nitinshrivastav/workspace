from addrecord import add_record
from checkresult import check_result
from collegeresult import college_result
from modifyresult import modify_result
def run():
    print('1 for add record')
    print('2 for check result')
    print('3 for college result')
    print('4 modify result')
    print('0 for exit')
    choice=input("Enter your choice")
    if(choice=='1'):
        add_record()
    elif(choice=='2'):
        check_result()
    elif(choice=='3'):
        college_result()
    elif(choice=='4'):
        modify_result()
    elif(choice=='0'):
        return 0
    else:
        print("Wrong choice")
start=1
while start !=0:
    start=run()