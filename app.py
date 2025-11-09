from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)  # 👈 Add this line

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# ✅ Feature columns used during training
expected_columns = [
    "reads_books", "weekly_hobby_hours",
    "hobby_top1_Badminton", "hobby_top1_Coding", "hobby_top1_Cricket",
    "hobby_top1_Dance", "hobby_top1_Debate", "hobby_top1_Football",
    "hobby_top1_Gym", "hobby_top1_Hackathons", "hobby_top1_Painting",
    "hobby_top1_Robotics", "hobby_top1_Writing",
    "club_top1_Coding Club", "club_top1_Cultural Club", "club_top1_Drama Club",
    "club_top1_Entrepreneurship Cell", "club_top1_Literary Club",
    "club_top1_Music Club", "club_top1_Robotics Club", "club_top1_Sports Club"
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Example JSON from frontend:
    # {
    #   "hobby_top1": "Coding",
    #   "club_top1": "Music Club",
    #   "reads_books": 1,
    #   "weekly_hobby_hours": 5
    # }

    # Initialize all columns with 0
    input_data = {col: 0 for col in expected_columns}

    # Set numeric columns
    input_data["reads_books"] = int(data["reads_books"])
    input_data["weekly_hobby_hours"] = int(data["weekly_hobby_hours"])

    # One-hot encode the categorical features
    hobby_col = f"hobby_top1_{data['hobby_top1']}"
    club_col = f"club_top1_{data['club_top1']}"
    
    if hobby_col in input_data:
        input_data[hobby_col] = 1
    if club_col in input_data:
        input_data[club_col] = 1

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Predict using the model
    prediction = model.predict(df)

    return jsonify({"prediction": prediction.tolist()})

if __name__ == "__main__":
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
