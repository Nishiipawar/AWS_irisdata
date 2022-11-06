import pickle
import json
import pandas as pd
import numpy as np
import config


class IrisFlower():
    def __init__(self, Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
        self.Id = Id
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm
       
    def load_model(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_iris_data(self):

        self.load_model() 
        array = np.zeros(len(self.json_data['columns']))
        array[0] = self.Id
        array[1] = self.SepalLengthCm
        array[2] = self.SepalWidthCm
        array[3] = self.PetalLengthCm
        array[4] = self.PetalWidthCm

        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print(f"flower is {predicted_charges}")
        return predicted_charges
        # if predicted_charges == 1 :
        #     print("the predicted flower species is")

        # else:
        #     print("try again")


        # prediction = "the predicted flower species is" if predicted_charges == 1 else "try again"

        # return prediction

if __name__ == "__main__":
    Id=1.0
    SepalLengthCm=5.1
    SepalWidthCm=3.5
    PetalLengthCm=1.4
    PetalWidthCm=0.2

    med_ins = IrisFlower(Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm)
    charges = med_ins.get_iris_data()