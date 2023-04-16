**Diabetes Prediction**
**This repository contains the code and data used to create a diabetes prediction model.**

**About the Project**
Diabetes is a chronic disease that affects millions of people worldwide. Early detection and management of the disease can significantly improve outcomes for patients. This project aims to create a machine learning model that can predict whether a patient is at risk of developing diabetes based on a set of clinical and demographic features.

The dataset used in this project is the Pima Indians Diabetes Database from Kaggle. It contains 768 observations and 8 features, including the outcome variable (whether or not a patient has diabetes).

##Requirements
To run the code in this repository, you will need the following Python packages:

pandas
numpy
scikit-learn
matplotlib
seaborn
You can install these packages using pip:
```pip install pandas numpy scikit-learn matplotlib seaborn```


##Usage
To reproduce the results of this project, run the diabetes_prediction.ipynb Jupyter notebook. This notebook contains all the code used to preprocess the data, train the machine learning model, and evaluate its performance.

The trained model is saved as a pickle file (diabetes_prediction_model.pkl). You can use this file to make predictions on new data.

##Results
The final model achieved an accuracy of 80% on the test set. The AUC-ROC score was 0.82.

##License
This project is licensed under the MIT License. See the LICENSE file for more information.

##Acknowledgments
The dataset used in this project was obtained from Kaggle: Pima Indians Diabetes Database
The code for this project was inspired by the Data Science Project from Scratch with Python tutorial by Susan Li.


