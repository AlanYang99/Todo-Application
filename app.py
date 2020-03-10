import db
import datetime
# print(datetime.now().day)
# print(datetime.now().month)
# print(datetime.now().year)


def addTodo(todo,day,month,year):
    con = db.connect()
    cur = con.cursor()
    cur.execute("select count(*) from todos")
    num = cur.fetchall()[0][0]
    print(type(day))
    query = """
    insert into todos (id,todo,date,status) values ({},'{}','{}',TRUE)
    """.format(num+1,todo,datetime.date(year,month,day))

    cur.execute(query)
    con.commit()

    con.close()
# addTodo('aadadaa',12,12,2020)
def completeTodo(todo):
    con = db.connect()
    cur = con.cursor()
    query = "delete from todos where id = '{}'".format(todo)
    cur.execute(query)
    con.commit()
    con.close()



def showList():
    con = db.connect()
    cur = con.cursor()
    cur.execute("select * from todos")
    rows = cur.fetchall()
    con.close()
    return rows


        # <!-- 
        #     <div class = "todo">
        #     <input type= "hidden" value="{{ row[1] }}"name= "complete" class = "item"> Hello </input>
        #     <input type="image" src = "../static/delete-icon.png" width = "20" height = "20" alt = "submit" class = "item"/>
        # </div>
        # <div class = "todo">
        #     <input type= "hidden" value="{{ row[1] }}"name= "complete" class = "item"> What </input>
        #     <input type="image" src = "../static/delete-icon.png" width = "20" height = "20" alt = "submit" class = "item"/>
        # </div> 
        # -->
        # <!--
        # {% for row in todos %}
        # <form action = "{{ url_for('delete')}}" method= "POST" class=delete-movie>
        #     <div class = "todo">
        #     <input type= "hidden" value="{{ row[1] }}"name= "complete"> {{row[1]}}</input>
        #     <input type="image" src = "../static/delete-icon.png" width = "20" height = "20" alt = "submit" />
        #     </div>
        # </form>
        # {% endfor %}
        # -->