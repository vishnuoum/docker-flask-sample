import json
import pickle
import gladiator as gl
from flask import Flask, request, Response
import os

app = Flask(__name__)

species = ['Setosa', 'Versicolor', 'Virginica']

validator = (
    ('sepal_len', gl.required, gl.type_(float)),
    ('sepal_width', gl.required, gl.type_(float)),
    ('petal_len', gl.required, gl.type_(float)),
    ('petal_width', gl.required, gl.type_(float))
)

def init():
    global model
    filename = os.path.join(os.getcwd(), 'models', 'model.pk')
    print(filename)
    with open(filename, "rb") as file:
        model = pickle.load(file)
    



def classify(sepal_len, sepal_width, petal_len, petal_width):
    species_class = model.predict([[sepal_len, sepal_width, petal_len, petal_width]])[0]
    return species[species_class]


@app.route("/classify", methods = ["POST"])
def classifyApi():
    data = request.get_json()
    app.logger.info(data)
    if(gl.validate(validator, data)):
        result = classify(
            petal_len=data["petal_len"],
            petal_width=data["petal_width"],
            sepal_len=data["sepal_len"],
            sepal_width=data["sepal_width"]
        )

        return Response(
            response=json.dumps({"species":result}),
            status=200,
            mimetype="application/json"
        )
    else:
        return Response(
            response="Validation Error",
            status=400,
        )

@app.get("/")
def greet():
    return Response(
        response="Hello"
    )

if(__name__ == "__main__"):
    init()
    app.run(host="0.0.0.0")
