from flask import Flask, request, render_template
import numpy as np
import pickle
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")

# Load models and scalers
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# Flask app setup
app = Flask(__name__)

# Crop Dictionary
crop_dict = {
    1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya",
    7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes",
    12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil", 16: "Blackgram",
    17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
    21: "Chickpea", 22: "Coffee"
}

# Home Route
@app.route('/')
def index():
    return render_template("index.html")

# Prediction Route
@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Retrieve and validate inputs
        N = float(request.form.get('Nitrogen', 0))
        P = float(request.form.get('Phosporus', 0))
        K = float(request.form.get('Potassium', 0))
        temp = float(request.form.get('Temperature', 0))
        humidity = float(request.form.get('Humidity', 0))
        ph = float(request.form.get('Ph', 0))
        rainfall = float(request.form.get('Rainfall', 0))

        # Prepare input features
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Scaling features
        scaled_features = ms.transform(single_pred)
        final_features = sc.transform(scaled_features)

        # Prediction
        prediction = model.predict(final_features)

        # Retrieve the crop recommendation
        crop = crop_dict.get(prediction[0], "Unknown Crop")
        result = f"{crop} is the best crop to be cultivated right there."

    except ValueError:
        result = "Invalid input: please enter valid numbers for all fields."
    except Exception as e:
        result = f"An error occurred during prediction: {e}"

    return render_template('index.html', result=result)

# Main function
if __name__ == "__main__":
    app.run(debug=True)


