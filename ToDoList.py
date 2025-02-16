import mysql.connector as mc
def connection():
    mydb=mc.connect(host='localhost',user='root',password='IMnj734204',database='new')
    return mydb

def create_task(taskid,heading,descr):
    mydb=connection()
    cur=mydb.cursor(dictionary=True)
    cur.execute("insert into tasks(tid, title, description) values(%s,%s,%s);",(taskid, heading, descr))
    mydb.commit()
    cur.close()
    mydb.close()

def read_task(title):
    mydb=connection()
    cur=mydb.cursor(dictionary=True)
    if(title=="a"):
        cur.execute("select * from tasks;")
    elif(title=="p"):
        cur.execute("select * from tasks where status='pending';")
    elif(title=="c"):
        cur.execute("select * from tasks where status='completed';")
    tasks=cur.fetchall()
    cur.close()
    mydb.close()
    return tasks

def update_task(tid,field,value):
    mydb=connection()
    cur=mydb.cursor(dictionary=True)
    sql=f"update tasks set {field}=%s where tid=%s;"
    cur.execute(sql,(value,tid))
    mydb.commit()
    cur.close()
    mydb.close()

def delete_task(tid):
    mydb=connection()
    cur=mydb.cursor(dictionary=True)
    cur.execute("delete from tasks where tid=%s;",(tid,))
    mydb.commit()
    cur.close()
    mydb.close()
    

count=2
l1=[1,2]
operation=int(input("enter the operation you want to perform: 1:Create \t 2:Read \t 3:Update \t 4:Delete \t 5:Exit:"))
match operation:
    case 1:
        taskid=int(input("enter the task id:"))
        if(taskid in l1):
            raise ValueError("This taskid already exists")
        else:
            l1.append(taskid)
            heading=input("enter the title of the task:")
            descr=input("enter the description of the task:")
            create_task(taskid,heading,descr)
            print("task created successfully")
        
    case 2:
        title=input("enter which tasks you want to view:  a:all \t p:pending \t c:completed:")
        if(title=='a' or title=='p' or title=='c'):
            tasks=read_task(title)
            for i in tasks:
                print(i)
        else:
            raise ValueError("not a valid value")
        
    case 3:
        tid=input("enter the taskid of the task:")
        if(tid not in l1):
            raise ValueError("This task id is not present")
        else:
            field=input("enter the column name:")
            value=input("enter the new value:")
            update_task(tid,field,value)
            print("task updated successfully")
        
    case 4:
        tid=int(input("enter the tid you want to delete:"))
        if(tid not in l1):
            raise ValueError("This task id is not present")
        else:
            delete_task(tid)
            print("task deleted successfully")
        
    case 5:
        print("you have exited")