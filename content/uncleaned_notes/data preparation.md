# Data Preparation for Machine Learning

[link](https://www.youtube.com/watch?v=P8ERBy91Y90)
## Introduction

Faulty datasets can skew results. This case highlights the critical importance of proper data preparation in machine learning. 

## Step-by-Step Data Preparation Process

### 1. Problem Formulation and Planning

Data preparation begins with a clear definition of the problem to be solved with machine learning. This step is similar to any other business decision-making process and sets the stage for constructing an appropriate training dataset.

### 2. Constructing the Training Dataset
**Dataset Size**
- **Determining Size**: The required size of the dataset varies based on the complexity of the problem and the learning algorithm used. Generally, more data is better, but the exact amount needed can vary significantly.

**Dataset Quality**
- The principle of =="garbage in, garbage out"== underscores the importance of high-quality data. Inaccurate or poor-quality data leads to poor model performance, regardless of the model's sophistication or the expertise of the data scientists.

### 3. Data Transformation
Data must be transformed into a format that is most suitable for the machine learning model. This includes several steps such as ==labeling, cleansing, and feature engineering.==

**Labelling**
- **Supervised Learning**: This involves annotating the dataset with the correct answers (labels) to teach the model. For example, labeling images of apples to distinguish them from other fruits.
- **Manual and Automated Labeling**: Manual labeling by humans or leveraging existing labeled data. Tools like Google’s reCAPTCHA help in building labeled datasets.

**Data Reduction and Cleansing**
- [[Dimension reduction]]: Remove features with zero or low variance and redundant features to improve model performance.
  - Example: Removing a 'country' feature when all data points are from the same country.
- **Sampling**: Use subsets of data for training to speed up the process and address issues like imbalanced data representation.
  - Example: Amazon's imbalanced dataset of mostly male resumes.

**Cleaning**:
- **Handling Missing Data**: Fill missing values with constants or predicted values.
- **Removing Corrupted Data**: Delete inaccurate or corrupted data entries.

### 4. Data Wrangling 
Transform raw data into a format that best describes the problem to the model. This includes formatting and normalization.

**Formatting**
- Convert data into the required format, e.g., from .xls to .csv.

 [[normalization]]
- Ensure consistent data representation and scale features appropriately.
  - Example: Normalize monetary values and quantities to a common scale using methods like min-max normalization.

### 5. Feature Engineering
Creating new features from existing data to better capture the underlying patterns.

**Example**:
- Decompose datetime information into separate features for date and time to capture their respective predictive powers.
