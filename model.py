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

    
class Movie():
    def play_movie():
        file_size = os.stat('static/media/ppil2.mp4').st_size
        start = 0
        length = 10240  # can be any default length you want

        range_header = request.headers.get('Range', None)
        if range_header:
            m = re.search('([0-9]+)-([0-9]*)', range_header)  # example: 0-1000 or 1250-
            g = m.groups()
            byte1, byte2 = 0, None
            if g[0]:
                byte1 = int(g[0])
            if g[1]:
                byte2 = int(g[1])
            if byte1 < file_size:
                start = byte1
            if byte2:
                length = byte2 + 1 - byte1
            else:
                length = file_size - start

        with open('static/media/ppil2.mp4', 'rb') as f:
            f.seek(start)
            chunk = f.read(length)

        rv = Response(chunk, 206, mimetype='video/mp4', content_type='video/mp4', direct_passthrough=True)
        rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(start, start + length - 1, file_size))
        return rv
        
    