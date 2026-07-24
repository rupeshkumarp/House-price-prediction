# House Price Prediction

A machine learning project that predicts house prices using the **Random Forest Regressor** algorithm. The project includes data preprocessing, feature engineering, model training, evaluation, and a runnable `app.py` for making house price predictions.

## Project Structure

* **app.py** – Main application used to load the trained model and predict house prices.
* **data_preprossing.ipynb** – Jupyter Notebook containing data cleaning, preprocessing, exploratory data analysis (EDA), feature engineering, and Random Forest model training.
* **predictions_data.csv** – Sample dataset used for training and testing the model.
* **logs/** – Directory containing logs, model outputs, or prediction results.

---

## Machine Learning Model

This project uses the **Random Forest Regressor**, an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

### Why Random Forest?

* Handles complex, non-linear relationships effectively.
* Produces accurate and reliable predictions.
* Reduces overfitting compared to a single Decision Tree.
* Performs well on regression tasks.

---

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, install the commonly used packages manually:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

---

## Quick Start

### 1. Run the preprocessing notebook

Open the notebook using Jupyter Notebook or JupyterLab:

```bash
jupyter notebook data_preprossing.ipynb
```

The notebook performs:

* Data Cleaning
* Missing Value Handling
* Feature Engineering
* Exploratory Data Analysis (EDA)
* Random Forest Model Training
* Model Evaluation

### 2. Run the application

```bash
python app.py
```

The application loads the trained Random Forest model and predicts house prices.

---

## How to Run

### Create and Activate a Virtual Environment

### Windows (Command Prompt)

```bash
python -m venv venv
venv\Scripts\activate.bat
```

### Install Dependencies
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter datetime logging
```

### Run the Application

```bash
python app.py
```

### Check Outputs

The generated outputs, logs, or predictions will be available in the **logs/** directory.

---

## Notebook

The notebook demonstrates the complete machine learning workflow, including:

* Data Cleaning
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Random Forest Model Training
* Model Evaluation
* House Price Prediction

---

## Dataset

`predictions_data.csv` contains the housing dataset used to train and evaluate the Random Forest Regression model.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Random Forest Regressor
* Jupyter Notebook
