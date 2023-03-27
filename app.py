from flask import Flask, render_template
from database import load_users_from_db
app = Flask(__name__)


@app.route("/")
def hello_world():
  users = load_users_from_db()
  return render_template('home.html',
                        users=users)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
