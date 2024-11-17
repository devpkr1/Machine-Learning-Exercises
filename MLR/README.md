# Multiple Linear Regression Analysis on Toyota Corolla Dataset

## Assignment Task
The objective of this analysis is to perform a multiple linear regression (MLR) to predict the price of Toyota Corolla based on various attributes.

## Dataset Description
The dataset consists of the following variables:
- **Age**: Age in years
- **KM**: Accumulated Kilometers on odometer
- **FuelType**: Fuel Type (Petrol, Diesel, CNG)
- **HP**: Horse Power
- **Automatic**: Automatic (Yes=1, No=0)
- **CC**: Cylinder Volume in cubic centimeters
- **Doors**: Number of doors
- **Weight**: Weight in Kilograms
- **Quarterly_Tax**: 
- **Price**: Offer Price in EUROs

## Tasks

### 1. Exploratory Data Analysis (EDA)

#### Summary Statistics
We will begin by loading the dataset and examining the summary statistics to understand the distribution of variables.

#### Visualizations
We will create visualizations to explore the relationships between the variables.

#### Data Preprocessing
- Handle categorical variables (e.g., FuelType)
- Check for missing values
- Normalize or standardize the numerical features if necessary

### 2. Split the Dataset
We will split the dataset into training (80%) and testing (20%) sets.

### 3. Build Multiple Linear Regression Models

#### Model 1: Basic MLR
We will create a linear regression model using the training dataset and interpret the coefficients.

#### Model 2: Including Interaction Terms
We will build a second model that includes interaction terms between variables.

#### Model 3: Polynomial Features
We will create a third model using polynomial features to capture non-linear relationships.

### 4. Evaluate Model Performance
We will evaluate the performance of the models using appropriate metrics on the testing dataset.

### 5. Apply Lasso and Ridge Regression
We will apply Lasso and Ridge regression methods to the models and compare their performance.

## Interview Questions

### 1. What is Normalization & Standardization and how is it helpful?

### 2. What techniques can be used to address multicollinearity in multiple linear regression?

**Ensure to properly comment your code and provide explanations for your analysis.**
**Include any assumptions made during the analysis and discuss their implications.**