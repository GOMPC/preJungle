from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbjungle


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/list', methods=['GET'])
def show_memo():
    memos = list(db.memos.find({}, {'_id': False}).sort('like', -1))
    return jsonify({'result': 'success', 'memo_list': memos})


@app.route('/api/like', methods=['POST'])
def like_memo():
    text_receive = request.form['text_give']

    memo = db.memos.find_one({'text': text_receive})

    new_like = memo['like'] + 1

    db.memos.update_one({'text': text_receive}, {'$set': {'like': new_like}})

    return jsonify({'result': 'success'})


@app.route('/api/delete', methods=['POST'])
def delete_memo():
    text_receive = request.form['text_give']
    db.memos.delete_one({'text': text_receive})
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
    pre_text = request.form['pre_text']

    title_receive = request.form['title_give']  
    text_receive = request.form['text_give']  

    db.memos.update_one({'text':pre_text},{'$set':{'title':title_receive, 'text':text_receive}})

    return jsonify({'result': 'success'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)