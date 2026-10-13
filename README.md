# 🛵 Swiggy Delivery Time Prediction

## 📌 Project Overview

The **Swiggy Delivery Time Prediction** project uses Machine Learning regression algorithms to predict food delivery time in minutes based on various factors, including weather conditions, traffic, vehicle type, delivery partner details, and other delivery-related attributes.

This project follows the **CRISP-ML(Q) methodology** to develop, evaluate, optimize, and deploy a Machine Learning model.

The goal is to support more accurate delivery time estimates, improve customer satisfaction, and help address delivery-related operational challenges.

## 🎯 Business Problem

Inaccurate delivery time predictions can lead to:

* Late deliveries and customer dissatisfaction.
* Increased customer complaints.
* Unrealistic delivery expectations.
* Pressure on delivery partners, potentially affecting road safety and service quality.

### 💡 Objective

Build a Machine Learning regression model that predicts estimated food delivery time in minutes using relevant delivery-related features.

## 📊 Dataset Information

* **Dataset size:** Approximately 45,000 records.
* **Problem type:** Supervised Machine Learning – Regression.
* **Target variable:** `time_taken` (delivery time in minutes).

## 🔄 Project Workflow – CRISP-ML(Q)

### 1. Data Understanding & Exploratory Data Analysis (EDA)

* Analyzed the dataset structure and feature distributions.
* Examined numerical and categorical variables.
* Explored patterns and relationships among delivery-related features.
* Identified data quality issues and missing values.

### 2. Data Preprocessing

**Missing Value Imputation**

* Used KNN Imputation to handle missing values in numerical features.
* Used Simple Imputer with the most frequent value to handle missing categorical values.

**Feature Encoding**

* **Ordinal Encoding:** Converted categorical features with a meaningful order into numerical representations.
* **Nominal Encoding:** Used One-Hot Encoding for categorical features without a natural order.

These steps prepared the dataset for Machine Learning model development.

### 3. Model Building

Developed and compared the following regression algorithms:

* Random Forest Regressor
* XGBoost Regressor

### 4. Model Evaluation

Evaluated the models using the following metrics:

* **R² Score:** Measures how well the model explains variation in delivery time.
* **Mean Absolute Error (MAE):** Measures the average absolute prediction error.
* **Mean Squared Error (MSE):** Measures the average squared prediction error.
* **Root Mean Squared Error (RMSE):** Measures prediction error in the target variable's units.

### 📈 Initial Model Results

| Model                   | R² Score |    MAE |
| ----------------------- | -------: | -----: |
| Random Forest Regressor |   0.8201 | 3.1648 |
| XGBoost Regressor       |   0.8212 | 3.1625 |

XGBoost achieved slightly better initial performance and was selected for further optimization.

### 5. Hyperparameter Tuning

Applied **Bayesian Optimization** to identify suitable XGBoost hyperparameters.

* Initial XGBoost R² Score: 0.8212
* Tuned XGBoost R² Score: 0.8328 (83.28%)

The tuned model achieved an improved R² score compared with the initial model.

*Note: Reported evaluation scores should correspond to the same evaluation procedure and dataset split when comparing model performance.*

### 6. Model Deployment

Deployed the trained Machine Learning model using **Streamlit** to create an interactive web application.

The application allows users to enter relevant delivery details and obtain a predicted delivery time in minutes.

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn
* **Model Optimization:** Bayesian Optimization
* **Boosting Algorithm:** XGBoost
* **Web Application:** Streamlit
* **Development Environment:** Jupyter Notebook

## 📂 Project Structure

```text
Swiggy-Delivery-Time-Prediction/
│
├── app.py                  # Streamlit application
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── swiggy_dtp.pkl          # Saved model, if using this filename
└── notebooks/
    └── model_training.ipynb # Model development and evaluation
```



## 📌 Key Learnings

* Understanding an end-to-end Machine Learning workflow.
* Performing Exploratory Data Analysis.
* Handling missing values using imputation techniques.
* Applying Ordinal Encoding and Nominal Encoding.
* Building and comparing regression models.
* Evaluating models using regression metrics.
* Optimizing hyperparameters using Bayesian Optimization.
* Deploying a Machine Learning model using Streamlit.

## 🚀 Future Improvements

* Evaluate model performance on additional unseen data.
* Monitor data drift and model performance over time.
* Incorporate additional delivery-related features where available.
* Improve prediction accuracy through further experimentation.
* Deploy the application to a cloud hosting platform.
