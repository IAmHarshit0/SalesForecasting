# 🛒 Sales Forecasting App

An end-to-end machine learning project to predict retail product sales using a custom dataset. This project combines data cleaning, feature engineering, model experimentation, and a deployable Streamlit frontend.

## 📌 Features

- Trains and evaluates **multiple regression models** to identify the best performer.
- Handles missing values and performs label encoding for categorical data.
- Engineers new features like `New_Item_Type` and `Outlet_Years`.
- Saves the best trained model and encoders for deployment.
- Provides a user-friendly Streamlit interface for making predictions.

## 🧠 Machine Learning Workflow

### 🔍 Models Compared

- **Linear Regression**
- **Ridge Regression**
- **Lasso Regression**
- **XGBoost Regressor**
- **LightGBM Regressor** _(best performing model used for deployment)_

### 🎯 Target Variable

- `Item_Outlet_Sales`

### ⚙️ Feature Engineering

- `Outlet_Years` = 2025 - `Outlet_Establishment_Year`
- `New_Item_Type` derived from `Item_Identifier`

### 🧼 Preprocessing

- Missing value imputation
- Label encoding for categorical features
- Feature selection and scaling (as needed)

### 📦 Model Persistence

- Best model saved to `model.pkl`
- Label encoders saved to `encode.pkl`

## 📊 Features Used in Prediction

1. `Item_Weight`
2. `Item_Fat_Content`
3. `Item_Visibility`
4. `Item_MRP`
5. `Outlet_Size`
6. `Outlet_Location_Type`
7. `Outlet_Type`
8. `New_Item_Type`
9. `Outlet_Years`
10. `Outlet` (encoded from `Outlet_Identifier`)

## 💻 Tech Stack

- **Notebook**: Jupyter (`.ipynb`)
- **Deployment**: Streamlit
- **Models**: scikit-learn, XGBoost, LightGBM
- **Utilities**: Pandas, NumPy, Pickle

## 🚀 How to Run the Project

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/sales-forecasting-app.git
cd sales-forecasting-app
```

2. **Install Required Packages**

```bash
pip install -r requirements.txt
```

3. **Train the Model (Optional)**

Run the Jupyter notebook `PRJ Sales Forecasting.ipynb` to:

- Preprocess the data
- Train multiple models
- Evaluate and select the best one
- Save the model (`model.pkl`) and encoders (`encode.pkl`)

4. **Run the Streamlit App**

```bash
streamlit run app.py
```

## 📁 Project Structure

```
sales-forecasting-app/
├── app.py                    # Streamlit frontend
├── PRJ Sales Forecasting.ipynb  # Notebook with full EDA, training, and evaluation
├── model.pkl                 # Best trained model (LightGBM)
├── encode.pkl                # Saved label encoders
├── Train.csv                  # Custom dataset (already available on GitHub)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## 📂 Dataset

- The dataset used in this project is a custom retail sales dataset, included in the repository as `Train.csv`.

## 📈 Example Output

- Model comparison results and RMSE scores for each
- Final prediction output shown in Streamlit
- Visuals for model performance (from the notebook)

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [LightGBM](https://lightgbm.readthedocs.io/)
