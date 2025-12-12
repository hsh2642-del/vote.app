from flask import Flask, render_template, request

app = Flask(__name__)

candidates = {}
total_voters = 0
current_voter = 1
invalid_votes = 0   # 무효표 카운트 추가!


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    global candidates, total_voters, current_voter, invalid_votes
    candidates = {}
    total_voters = 0
    current_voter = 1
    invalid_votes = 0

    num = int(request.form['num'])
    for i in range(1, num + 1):
        name = request.form.get(f'candidate{i}')
        if name:
            candidates[name] = 0

    return render_template('voters.html')


@app.route('/voters', methods=['POST'])
def voters():
    global total_voters
    total_voters = int(request.form['voters'])
    return render_template('vote.html', candidates=candidates, current=1)


@app.route('/vote', methods=['POST'])
def vote():
    global candidates, total_voters, current_voter, invalid_votes

    vote_name = request.form.get('candidate')
    current_voter = int(request.form['current'])

    # 무효표 처리
    if vote_name not in candidates:
        invalid_votes += 1
    else:
        candidates[vote_name] += 1

    current_voter += 1

    # 투표 모두 완료
    if current_voter > total_voters:
        return render_template(
            'result.html',
            candidates=candidates,
            invalid=invalid_votes
        )

    # 아직 투표 남음
    return render_template('vote.html', candidates=candidates, current=current_voter)


if __name__ == '__main__':
    app.run(debug=True)
