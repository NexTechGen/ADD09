from flask import Flask, render_template, request, redirect, url_for
from getData import taab

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
      return render_template(
          "data.html",
          tables=[
              data.to_html(
                  classes=
                  'table-sm table table-hover container-sm table-bordered',
                  header="true",
                  index='false')
          ][0])
    else:
      return render_template("index.html")
  except:
    return render_template("index.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
