from flask import Flask, jsonify

app = Flask(__name__)   # Flask 객체 생성

def add_file(data):
    return data + 5 

@app.route("/hello", methods = ['GET'])    # 라우트 설정
def hello():
    return f"<h1>Hello</h1>"

@app.route('/profile/<username>')   #파라미터 인자
def get_profile(username: str) -> str:
    return "profile:" + username

@app.route('/message/<int:message_id>') #파라미터 인자 받을때 타입 힌트를 적용가능
def get_message(message_id: int) -> int:
    return "message id: %d" % message_id

@app.route("/first/<int:messageid>")
def get_first(messageid):
    data = add_file(messageid)
    return "<h1>%d</h1>" % (data)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port="8082");