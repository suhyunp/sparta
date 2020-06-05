from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('shopping.html')


## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def make_order():
    name_receive = request.form['name_give']
    number_receive = request.form['number_give']
    adress_receive = request.form['adress_give']
    cellphone_receive = request.form['cellphone_give']

    review = {
       'name': name_receive,
       'number': number_receive,
       'adress': adress_receive,
       'cellphone': cellphone_receive
    }

    db.reviews.insert_one(review)
    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다..'})


@app.route('/reviews', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id':0}))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)