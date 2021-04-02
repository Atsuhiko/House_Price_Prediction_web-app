# 参考: https://qiita.com/redshoga/items/60db7285a573a5e87eb6
# 参考: https://teratail.com/questions/244325
# 参考: https://qiita.com/Susasan/items/52d1c838eb34133042a3

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g, flash
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def upload_file():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":

        x1 = request.form["GrLivArea"]
        x2 = request.form['GarageCars']
        x3 = request.form['TotalBsmtSF']
        x4 = request.form['BsmtFinSF1']
        x5 = request.form['1stFlrSF']

        X = [[x1, x2, x3, x4, x5]] # 2次元の行列

        # 予測
        # https://www.sairablog.com/article/pickle-trained-model-save-read.html
        model = pickle.load(open('model.pickle', 'rb')) # 学習ずみモデルの読み込み
        pred = int(model.predict(X)[0]) # 行列から要素を取り出し

        return  render_template("index.html", pred=pred)

if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=4444) # ポートの変更
