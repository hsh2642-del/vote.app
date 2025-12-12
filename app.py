from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/set_candidates", methods=["POST"])
def set_candidates():
    try:
        num = int(request.form["candidate_count"])
    except:
        return "후보 수는 숫자여야 합니다."

    candidate_names = []
    for i in range(num):
        candidate_names.append(request.form.get(f"candidate_{i}"))

    # 무효표 추가
    candidate_names.append("무효표")

    return render_template("vote.html", candidates=candidate_names)


@app.route("/vote", methods=["POST"])
def vote():
    candidates = request.form.getlist("candidates")
    try:
        voters = int(request.form["voter_count"])
    except:
        return "유권자 수는 숫자여야 합니다."

    # 후보 목록
    candidate_names = request.form.getlist("candidate_names")

    # 득표수 초기화
    results = {name: 0 for name in candidate_names}

    # 투표 반영
    for i in range(voters):
        vote = request.form.get(f"vote_{i}")
        if vote in results:
            results[vote] += 1

    # 최고 득표자 계산
    max_votes = max(results.values())
    winners = [name for name, v in results.items() if v == max_votes]

    return render_template("result.html", results=results, winners=winners, max_votes=max_votes)
  

if __name__ == "__main__":
    app.run()
