from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjungle


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def show_memo():
    memos = list(db.memos.find().sort('like', -1))
    
    return jsonify({'result': 'success', 'memo_list': dumps(memos)})


@app.route('/api/like', methods=['POST'])
def like_memo():
    id_receive = request.form['id_give']

    memo = db.memos.find_one({'_id': ObjectId(id_receive)})

    new_like = memo['like'] + 1

    db.memos.update_one({'_id': ObjectId(id_receive)}, {'$set': {'like': new_like}})

    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def delete_memo():
    id_receive = request.form['id_give']
    db.memos.delete_one({'_id': ObjectId(id_receive)})
    return jsonify({'result': 'success'})

@app.route('/memo', methods=['POST'])
def post_memo():
    title_receive = request.form['title_give'] 
    text_receive = request.form['text_give']

    memo = {'title': title_receive, 'text': text_receive, 'like': 0}

    db.memos.insert_one(memo)

    return jsonify({'result': 'success'})

@app.route('/memo/edit', methods=['POST'])
def edit_memo():
    id_receive = request.form['id_give']

    get_memo = db.memos.find_one({'_id': ObjectId(id_receive)})

    return jsonify({'result': 'success', 'memo_get': dumps(get_memo)})

@app.route('/memo/clear', methods=['POST'])
def edit_clear_memo():
    id_receive = request.form['id_give']

    title_receive = request.form['title_give']  
    text_receive = request.form['text_give']  

    db.memos.update_one({'_id': ObjectId(id_receive)},{'$set':{'title':title_receive, 'text':text_receive}})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)