from flask import Flask, Response , request, render_template 
from flask_cors import CORS
import json
import uuid

app = Flask(__name__,static_url_path='/static')

CORS(app)

# /method?argumen1=value1&argumen2=value2

users = {}

@app.route("/")
def main():
    return render_template ('index.html')


@app.route("/auth")
def auth():  
    new_user = request.args.get('name')
# name !+ '' or None
    if new_user == '' or new_user == None:
        return 'Отмена'
    if users.get(new_user) != None:
        return 'Такой пользователь уже есть'
    myuuid = uuid.uuid4()
    users[new_user]= str(myuuid)
    return str(myuuid)

@app.route("/logout")
def logout():
    token = request.args.get('token')
    for key, value in users.items():
        if value == token:
            del users[key]
            return 'крутаааа вышел'
    return 'ощепка'


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
     
    return 'err'
   

@app.route("/getall")
def getall():
    token = request.args.get('token')
    if token not in users.values():
        return Response('шашлыки', status = 403, minetype='text/plain')
    x = [
        {'name': 'Max', 'message': '', 'timestamp':123},
    ]
    return Response(json.dumps(x), status=200)


if __name__ == "__main__":
    print('RABOTAEM')
    {app.run(debug=True)}