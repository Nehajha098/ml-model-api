# Hobby Hours Forecaster for Hackathons 🎯

##  Project Overview
This project predicts students’ **weekly hobby/coding hours**, helping hackathon organizers build balanced teams by estimating coding effort.

Built using survey responses from SNU students via a Google Form, the model leverages ML techniques like Random Forest and Gradient Boosting.

---

##  Steps Implemented
1. **Data Cleaning & Processing**  
2. **Encoding Categorical Features**  
3. **Train-Test Split**  
4. **Model Training & Hyperparameter Tuning** (Random Forest & Gradient Boosting)  
5. **Feature Importance Analysis**  
6. **Model Comparison & Ensemble**  
7. **Model Saving & Prediction on New Data**

---

##  Evaluation Results

- **Random Forest (Tuned)**  
  -  MAE: ~9.3  
  -  RMSE: ~11.15  
  -  R²: ~0.11  

- **Gradient Boosting (Tuned)**  
  -  MAE: ~9.7  
  -  RMSE: ~11.95  
  -  R²: ~–0.02  

- **Ensemble (RF + GB)**  
  -  MAE: ~9.5  
  -  RMSE: ~11.4  
  -  R²: ~0.07  

**Conclusion:** Random Forest emerged as the best performer for this dataset.
Team Plan – Coding Hours Forecaster

Team Members:

Neha Jha

Repository setup & GitHub management

Documentation (README, requirements.txt)

Project coordination

Rumana Kar

Data cleaning & preprocessing

Feature encoding & train-test split

Model training (Random Forest, Gradient Boosting) with hyperparameter tuning

Feature importance visualization

Ensemble model comparison

Model saving & prediction demo

---

##  How to Run

```bash
# Clone project
git clone https://github.com/Nehajha098/Machine-Learning-Project-1.git
cd Machine-Learning-Project-1

# Install dependencies
pip install -r requirements.txt

# Run the prediction demo
python scripts/step7_model_save_predict.py
