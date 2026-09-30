a='C://Users//Fatemeh//Desktop//file//users.txt'
def add_user():
    username=input(' username:')
    user_id=input('Enter user ID:')
    status=input('Enter status :')
    file=open(a,'r')
    for line in file:
        data=line.strip().split(',')
        if data[0]==username:
            file.close()
            print('کاربر از قبل وجود دارد')
            return
    file.close()
    file=open(a,'a')
    file.write('\n'+username+','+user_id+','+status)
    file.close()       
    print('کاربر با موفقیت اضافه شد')
def find_user():
    username=input('Enter username  find:')
    file=open(a,'r')
    for line in file:
        data=line.strip().split(',')
        if data[0]==username:
            print('Username:',data[0])
            print('ID:',data[1])
            print('Status',data[2])
            file.close()
            return
    file.close()
    print('کاربر پیدا نشد')      
def delete_user():
    username=input('Enter username  delete:')
    file=open(a,'r')
    lines=file.readlines()
    file.close()
    found=False
    new_lines=[]
    for line in lines:
        data=line.strip().split(',')
        if data[0]==username:
            found=True
        else: 
            new_lines.append(line)
    file=open(a,'w')
    for line in new_lines:
        file.write(line) 
    file.close() 
    if found:
        print('کاربر با موفقیت حذف شد')
    else:
        print('کاربر پیدا نشد')
def generate_report():
    file=open(a,'r')
    active_users=0 
    blocked_users=0  
    for line in file:
        data=line.strip().split(',')
        if data[2]=='active':
            active_users+=1
        elif data[2]=='blocked':
            blocked_users+=1
    file.close()
    print('Active users:',active_users)
    print('Blocked users:',blocked_users)
add_user()
find_user() 
delete_user() 
generate_report()
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        