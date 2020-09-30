import sqlite3


def add_user(username, password):
        connection = sqlite3.connect("todo.db", check_same_thread=False)
        cursor = connection.cursor()
        cursor.execute("""
                    SELECT password
                    FROM users
                    WHERE username='{username}';""".format(
                        username=username
                    )
            
                )
        exists = cursor.fetchone()
        if exists is None:
            cursor.execute("""
                    INSERT INTO users(
                        username,
                        password
                        )VALUES('{username}', '{password}');""".format(
                            username=username,
                            password=password
                        )
                    )
             
            connection.commit()
            cursor.close()
            connection.close()
        
        else:
            return "User already exists"
        return "signed up successfully!"
    

def check_usernames(username):
    connection = sqlite3.connect("todo.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT username
                   FROM users;"""
        )
    db_user = cursor.fetchall()
    users = []
    for i in db_user:
        person = i[0]
        users.append(person)
        
    connection.commit()
    cursor.close()
    connection.close()
    
def check_pwd(username):
    connection = sqlite3.connect("todo.db", check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT password
                   FROM users
                   WHERE username = '{username}'
                   ORDER BY pk DESC;""".format(
                       username=username
                   )
                )
            
    password = cursor.fetchone()
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return password

def add_task(task, due_date):
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""
                    INSERT INTO tasks(
                        task,
                        due_date
                    )VALUES('{task}', '{due_date}');""".format(
                        task=task,
                        due_date=due_date
                    )
                )
    connection.commit()
    cursor.close()
    connection.close()
    return "entry added"    

def get_tasks():
    connection = sqlite3.connect('todo.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT *
                   FROM tasks
                   ;"""
                    
                )
        
    data = [i for i in cursor.fetchall()]
    # data = [i for i in all_columns]
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return data

    
    
    