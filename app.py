from flask import Flask, render_template, request

app = Flask(__name__)

# 메인 페이지 (후보 및 투표 입력)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 후보 목록 받아오기
        candidates = request.form.get("candidates").split()
        voters = int(request.form.get("voters"))

        # 투표할 때 후보별 투표수 0으로 초기화
        vote_counts = {c: 0 for c in candidates}
        return render_template("vote.html", candidates=candidates, voters=voters, vote_counts=vote_counts)

    return render_template("index.html")


# 투표 제출
@app.route("/vote", methods=["POST"])
def vote():
    candidates = request.form.getlist("candidate")
    vote_counts = {}

    # 후보별 득표 계산
    for c in candidates:
        if c not in vote_counts:
            vote_counts[c] = 0
        vote_counts[c] += 1

    # 최고 득표자 찾기
    max_votes = max(vote_counts.values())
    winners = [name for name, count in vote_counts.items() if count == max_votes]

    return render_template("result.html", vote_counts=vote_counts, max_votes=max_votes, winners=winners)


if __name__ == "__main__":
    app.run(debug=True)
