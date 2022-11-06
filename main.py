# from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import IrisFlower
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("WELCOME TO IRIS DATASET")
    return render_template("index.html")

@app.route('/predict_flower',methods=["POST","GET"])
def get_iris_prediction():

    if request.method == "GET":
        print("We are using GET Method")
        # data = request.form
        # print("Data::,data")
        Id = eval(request.args.get("Id"))
        SepalLengthCm = eval(request.args.get("SepalLengthCm"))
        SepalWidthCm= eval(request.args.get("SepalWidthCm"))
        PetalLengthCm= eval(request.args.get("PetalLengthCm"))
        PetalWidthCm= eval(request.args.get("PetalWidthCm"))

        print("Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm\n",Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

        med_ins = IrisFlower(Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        charges = med_ins.get_iris_data()

        return render_template("index.html", prediction = charges)
    else:
        print("We are using POST Method")

        Id = eval(request.form.get("Id"))
        SepalLengthCm = eval(request.form.get("SepalLengthCm"))
        SepalWidthCm= eval(request.form.get("SepalWidthCm"))
        PetalLengthCm= eval(request.form.get("PetalLengthCm"))
        PetalWidthCm= eval(request.form.get("PetalWidthCm"))
        
        print("Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm\n",Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)

        med_ins = IrisFlower(Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
        charges = med_ins.get_iris_data()

        return render_template("index.html", prediction = charges)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port=config.PORT_NUMBER, debug=True)