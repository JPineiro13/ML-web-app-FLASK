from flask import Flask, render_template, request
import pickle
import numpy as np

# Carga el modelo
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            features = [
                float(request.form['temp']),
                float(request.form['humidity']),
                float(request.form['wind']),
                float(request.form['pressure'])
            ]
            prediction = model.predict([features])[0]
        except:
            prediction = "Error en los datos ingresados"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)