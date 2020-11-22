class Terminate(Exception):
   pass

class Connection(Exception):
    pass


def write_to_file(f_obj):
    while True:
        try:
            x = yield
            f_obj.writelines(x)
            f_obj.writelines('\n')
        except Terminate:
            break
    f_obj.close()

def connect_user(username):
    with open('message.txt','w') as f:
        yield from write_to_file(f)



def task_planner():
    users = []
    while True:
        try:
            username = yield
            users.append(username)
        except Connection:
            yield from connect_user(users)


coroutine = task_planner()
next(coroutine)
coroutine.send('username1')
coroutine.send('username2')
coroutine.throw(Connection)
coroutine.send('message1')
coroutine.send('message2')
coroutine.throw(Terminate)
coroutine.close()
