from flask import Flask, render_template, request

app = Flask(__name__)

candidates = {}   # 후보 저장
votes = {}        # 후보별 표 저장

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    global candidates, votes
    num = int(request.form['num'])
    candidates = {}
    votes = {}

    # 후보 자동 생성 (웹버전은 입력창 추가하려면 더 만들 수 있음)
    for i in range(1, num + 1):
        name = request.form.get(f'candidate{i}')
        if name:
            candidates[name] = 0

    return render_template('vote.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    global candidates
    vote_name = request.form['candidate']

    if vote_name in candidates:
        candidates[vote_name] += 1

    return render_template('result.html', candidates=candidates)

if __name__ == '__main__':
    app.run()
