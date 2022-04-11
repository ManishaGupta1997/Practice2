from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
Swagger(app)

pickled_model = open("pickle_iris_model.pkl","rb")
classifier = pickle.load(pickled_model)

@app.route('/')  #decorators
def home():
    return "Welcome to iris classifier"

@app.route('/predict')
def predict_flower():

    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: sepal_width
          in: query
          type: number
          required: true  
        - name: sepal_length
          in: query
          type: number
          required: true
          name: petal_width
          in: query
          type: number
          required: true
          name: petal_length
          in: query
          type: number
          required: true

    responses:
        200:
            description: The result is    
    """

    sw = request.args.get("sepal_width")
    sl = request.args.get("sepal_length")
    pw = request.args.get("petal_width")
    pl = request.args.get("petal_length")

    result = classifier.predict([[sw,sl,pw,pl]])

    return f"The flower prediction is{result}"

if __name__ == "__main__":
    app.run()