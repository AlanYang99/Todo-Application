#!/usr/bin/env python3

from flask import Flask,render_template,request,url_for,redirect
from app import showList,addTodo,completeTodo
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html',todos = showList() )

@app.route('/',methods = ['POST','GET'])
def add():
    if request.method == 'POST':
        result = request.form['todo']
        addTodo(result,datetime.now().day,datetime.now().month,datetime.now().year)
    return render_template('home.html',todos = showList())

@app.route('/hello',methods = ['POST','GET'])
def delete():
    if request.method == 'POST':
        if 'complete.x' in request.form:
            pass
        elif 'delete.x' in request.form:
            result = request.form['delete']
            completeTodo(result)
    return redirect(url_for('main'))


@app.route('/baby',methods = ['POST','GET'])
def win():
    if request.method == 'POST':

        result = request.form.post['delete']
        print(result)
        completeTodo(result)
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(debug=True)