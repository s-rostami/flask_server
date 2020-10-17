from flask import Flask, escape, request, jsonify, render_template, redirect
from flask_cors import CORS
import pymysql


app = Flask(__name__)
CORS(app)

conn = pymysql.connect(
    host='ntier.cvvkrojoestg.us-east-1.rds.amazonaws.com',
    user="admin",
    port=int(3306),
    passwd="password",
    db="ntier",
    charset='utf8mb4')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        req_Json = request.json
        name1 = req_Json['Name']
        print(name1)
        email1 = req_Json['Email']
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users(name, email) VALUES(%s, %s)", (name1, email1))
        conn.commit()
        cur.close()
        return jsonify({"response": "hi" + name1})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
