# Logistic Regression

## 1. Data Exploration:

### a. Load the dataset and perform exploratory data analysis (EDA).
- Use libraries like `pandas` and `numpy` to load the dataset.
- Utilize `pandas` to display the first few rows of the dataset and check for any anomalies.

### b. Examine the features, their types, and summary statistics.
- Use `df.info()` to check feature types.
- Use `df.describe()` to get summary statistics for numerical features.

### c. Create visualizations to visualize distributions and relationships between features.
- **Histograms**: Use `matplotlib` or `seaborn` to create histograms for continuous features.
- **Box Plots**: Visualize the distribution and identify outliers.
- **Pair Plots**: Use `seaborn.pairplot()` to visualize relationships between features.
- **Analysis of Patterns**: Look for correlations using `df.corr()` and visualize with a heatmap.

## 2. Data Preprocessing:

### a. Handle missing values (e.g., imputation).
- Identify missing values using `df.isnull().sum()`.
- Use techniques like mean, median, or mode imputation to fill missing values.

### b. Encode categorical variables.
- Use `pd.get_dummies()` or `LabelEncoder` from `sklearn` to convert categorical variables into numerical format.

## 3. Model Building:

### a. Build a logistic regression model using appropriate libraries.
- Import `LogisticRegression` from `sklearn.linear_model`.
- Initialize the model: `model = LogisticRegression()`.

### b. Train the model using the training data.
- Split the data into training and testing sets using `train_test_split`.
- Fit the model: `model.fit(X_train, y_train)`.

## 4. Model Evaluation:

### a. Evaluate the performance of the model on the testing data.
- Use metrics such as:
  - **Accuracy**: `accuracy_score(y_test, y_pred)`
  - **Precision**: `precision_score(y_test, y_pred)`
  - **Recall**: `recall_score(y_test, y_pred)`
  - **F1-score**: `f1_score(y_test, y_pred)`
  - **ROC-AUC score**: `roc_auc_score(y_test, y_pred)`

### Visualize the ROC curve.
- Use `roc_curve` from `sklearn.metrics` to plot the ROC curve.

## 5. Interpretation:

### a. Interpret the coefficients of the logistic regression model.
- Coefficients represent the log-odds of the dependent variable for a one-unit increase in the predictor.

### b. Discuss the significance of features in predicting the target variable.
- Analyze the p-values or confidence intervals for the coefficients to determine significance.

## 6. Deployment with Streamlit:

### Create a Streamlit app in Python.
- Load the trained model using `joblib` or `pickle`.
- Set up user inputs using `st.sidebar` for predictions.

### Deployment options:
- **Local Deployment**: Run the app locally using `streamlit run app.py`.
- **Online Deployment**: Use Streamlit Community Cloud for online deployment.
  - Follow the instructions to create and deploy your app via GitHub.

## Interview Questions:

### 1. What is the difference between precision and recall?
- **Precision**: The ratio of true positive predictions to the total positive predictions (true positives + false positives).
- **Recall**: The ratio of true positive predictions to the total actual positives (true positives + false negatives).

### 2. What is cross-validation, and why is it important in binary classification?
- **Cross-validation**: A technique to assess how the results of a statistical analysis will generalize to an independent dataset. It involves partitioning the data into subsets, training the model on some subsets, and validating it on others.
- **Importance**: It helps in mitigating overfitting and provides a more reliable estimate of model performance.