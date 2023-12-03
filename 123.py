
from flask import Flask, Response , request
from flask_cors import CORS
import uuid



app = Flask(__name__)
CORS(app)

# /method?argumen1=value1&argumen2=value2

users = {}

@app.route("/")
def main():
    return "commands: /auth, /logout, /send, /getall"

@app.route("/auth")
def auth():  
    new_user = request.args.get('name')
# name !+ '' or None
    if new_user == '' or new_user == None:
        return 'Отмена'
    if users.get(new_user) != None:
        return 'Такой пользователь уже есть'
    myuuid = uuid.uuid4()
    users[new_user]= str(myuuid
    return str(myuuid)

@app.route("/logout")
def logout():
    token = request.args.get('token')
    for key, value in users.items():
        if value == token:
            del users[key]
            return 'Пользователь вышел из чата'
    return 'Ошибка'


@app.route("/send")
def send():
    text = request.args.get('text')
    token = request.args.get('token')
    print(text,token,users)
    if text == '':
        return 'Отмена'
    if token == '' or token == None:
        return 'Отмена'
    
    for key, value in users.items():

       if value == token:
            return text
     
    return 'Ошибка'
   

@app.route("/getall")
def getall():
    x = [
        {'name': 'Max', 'message': '', 'timestamp':123},
    ]
    return "Hello, World!"


if __name__ == "__main__":
    print('Работает')
    {app.run(debug=True)}