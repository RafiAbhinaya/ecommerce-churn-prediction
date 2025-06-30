# **Ecommerce Customer Churn Analysis and Prediction**

## Repository Outline
This repository consists of these following files:
- notebook.ipynb - Notebook documenting the EDA and model training.
- E Commerce Dataset.xsls - Dataset used for EDA and model training.
- final_model.pkl - The chosen model after evaluation
- url.txt - link to deployment
- deployment - directory to store files for deployment

## Problem Background
In e-commerce, retaining customers is just as important as attracting new ones, as customers are the main source of revenue. When users stop purchasing through the platform—a phenomenon called churn—the company risks losing significant income. To minimize churn, businesses can predict which customers are likely to leave and take proactive steps to retain them. Building a churn prediction program can therefore help improve customer retention and protect revenue.

In this project, we will train a model that will be able to predict the likeliness of a customer to churn.


## Project Output
This projects output is a model that's able to predict the likeliness of a customer to churn. The model is then deployed through streamlit, link to the deployment can be accessed [here](https://ecommerce-churn-prediction-rafiabhinaya.streamlit.app/).

## Data
The dataset used in this project is the **Ecommerce Customer Churn Analysis and Prediction** obtained from Kaggle. This dataset contains various Ecommerce user's information, such as gender, order count, etc. Each customer also has a label indicating whether they churned or not. The dataset consists of 5630 rows and 20 columns. Link to the dataset can be accesed [here](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data).

## Method
In this project, I trained multiple models using multiple supervised learning algorithms, which are KNN, SVM, decision tree, random forest, and XGBoost. In the end, the XGBoost model provided the best and most consistent results. After that, I deployed the model using Huggingface so others can try it out.

## Stacks
In the notebook, I used the following libraries to support my analysis and modeling:
- `Pandas` & `NumPy` – For data manipulation and numerical operations.  
- `Scipy Stats` – For statistical testing.  
- `Matplotlib.pyplot` & `Seaborn` – For data visualization.  
- `Scikit-learn` – For data preprocessing, model building (`RandomForestClassifier`, `KNeighborsClassifier`, `DecisionTreeClassifier`, `SVC`), evaluation, and hyperparameter tuning.  
- `XGBoost` – For gradient boosting classification with `XGBClassifier`.  
- `Cloudpickle` – For saving and loading the trained model.
- `Streamlit` - For creating the web app for deployment.

For deployment, I used streamlit cload.


## Reference
- Dataset link: [Ecommerce Customer Churn Analysis and Prediction](https://www.kaggle.com/datasets/ankitverma2010/ecommerce-customer-churn-analysis-and-prediction/data)
- Deployment link: [ecommerce-churn-prediction](https://huggingface.co/spaces/RafiAbhinaya/ecommerce-churn-prediction)