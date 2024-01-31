from flask import Flask, render_template, request, redirect, url_for
from getData import taab, House_Num

app = Flask(__name__)


@app.route('/')
def home():
  return render_template("index.html")


@app.route('/gettab', methods=["GET", "POST"])
def tPage():
  try:
    if request.method == "POST":
      nic = request.form.get('nic')
      print(nic)
      data = taab(nic)
      h_nums = House_Num(nic)
      return render_template(
          "data.html",
          tables=[
              data.to_html(
                  classes=
                  'table-sm table table-hover container-sm table-bordered',
                  header="true",
                  index='false')
          ][0],
          HS_num=h_nums)
    else:
      return render_template("index.html")
  except:
    return render_template("index.html")


@app.route('/log')
def login():
  return render_template('login.html')


@app.route('/admn', methods=["GET", "POST"])
def admin():
  try:
    if request.method == "POST":
      pwd = request.form.get('pwd')
      print(pwd)
      return render_template('login.html')
    else:
      return render_template('login.html')
  except:
    return render_template('index.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
