
# Used Car Resale Price Prediction | Machine Learning

##  Project Overview
Developed a Machine Learning regression model to predict the resale prices of used cars based on features such as brand, model, manufacturing year, mileage, fuel type, transmission and other vehicle specifications. The project focuses on data preprocessing, exploratory data analysis, model development, evaluation and hyperparameter tuning.

##  Project Objectives
- Predict used car resale prices.
- Identify important factors influencing vehicle prices.
- Compare multiple regression algorithms.
- Improve prediction performance through hyperparameter tuning.

##  Technologies Used
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

##  Project Workflow

### 1. Data Collection
Imported the used car dataset containing vehicle specifications and resale price information using Pandas.

### 2. Data Understanding
- Examined dataset dimensions, columns and data types.
- Generated statistical summaries.
- Identified missing values and duplicate records.
- Analyzed numerical and categorical features.

### 3. Data Cleaning
- Handled missing values.
- Removed duplicate records where necessary.
- Corrected inconsistent data.
- Identified and treated outliers where appropriate.
- Converted columns into suitable data types.

### 4. Exploratory Data Analysis (EDA)
- Analyzed used car price distributions.
- Studied the relationship between vehicle age and resale price.
- Examined the impact of mileage, fuel type and transmission.
- Used visualizations to identify patterns and relationships.

### 5. Feature Engineering
- Extracted useful information from existing features.
- Encoded categorical variables into numerical formats.
- Selected relevant features for model development.
- Removed irrelevant columns where appropriate.

### 6. Data Preprocessing
- Separated independent variables (X) and dependent variable (y).
- Applied categorical encoding.
- Scaled numerical features where required.
- Split data into training and testing datasets.

### 7. Model Building
Implemented and compared the following regression algorithms:

- **Linear Regression:** Built a baseline regression model.
- **Decision Tree Regressor:** Captured nonlinear relationships using decision-tree splitting.
- **Random Forest Regressor:** Combined multiple decision trees to improve prediction performance.
- **XGBoost Regressor:** Applied gradient boosting to improve predictive accuracy.

### 8. Model Evaluation
Evaluated model performance using the following metrics:

- **MAE:** Measures average absolute prediction error.
- **MSE:** Measures average squared prediction error.
- **RMSE:** Measures prediction error in the target variable's unit.
- **R² Score:** Measures the proportion of target variance explained by the model.

Compared the performance of different regression algorithms to identify the best-performing model.

### 9. Hyperparameter Tuning
Applied hyperparameter tuning using RandomizedSearchCV/GridSearchCV to identify optimal model parameters.

Used cross-validation to evaluate different parameter combinations and improve model performance.

### 10. Final Model Selection
Selected the best-performing regression model based on evaluation metrics and prediction performance on unseen test data.

##  Key Learnings
- Gained practical experience in end-to-end Machine Learning.
- Improved understanding of data preprocessing and feature engineering.
- Learned to implement and compare regression algorithms.
- Understood model evaluation and cross-validation.
- Gained experience in hyperparameter optimization.

##  Conclusion
Successfully developed a Machine Learning regression workflow to predict used car resale prices. Compared multiple regression algorithms, evaluated their performance and applied hyperparameter tuning to improve prediction accuracy.

##  Author
**Yasala Akshitha**
