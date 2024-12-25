
# Real Estate Price Predictor

This project is a Real Estate Price Predictor that uses a machine learning model to predict the prices of houses based on their features. The model has been trained on a dataset containing various features such as the number of rooms, property age, and other relevant information.


## Features

- Data preprocessing: Data cleaning, imputation, and feature scaling.

- Machine learning models: Trained using Random Forest Regressor, with an option to test other models like Linear Regression and Decision Tree Regressor.

- Model evaluation: Evaluates model performance using RMSE (Root Mean Squared Error) and cross-validation.



## Requirements
- Python 
- Pandas for data manipulation
- NumPy for numerical operations
- Scikit-Learn for machine learning algorithms and data preprocessing
- Matplotlib for data visualization
- Joblib for model serialization
You can install these using:
```bash
 pip install pandas numpy scikit-learn matplotlib joblib
```
## Installation

1. Clone the Repository
```bash
  git clone https://github.com/HarishLoni/HousePrice_Predictor.git
  cd HousePrice_Predictor
```
2. Prepare Your Data
- Ensure your data file (e.g., data.csv) is in the same directory or specify the path in your code.

3. Run the Code
- Run the script to train and test the model:
```bash
python train_model.py
```
Note: Replace train_model.py with the actual script name if it's different.

4. Run the Django App (if applicable)
- To start the Django web app for predictions Navigate to the Django project directory:
```bash
cd predictor
```
- Run the Django server:
```bash
python manage.py runserver
```
Access the app at http://127.0.0.1:8000/ in your web browser.

