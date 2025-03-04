https://github.com/rhyslwells/ML_Tools/tree/main/Explorations\Selection\ROC_Curve.py
## **Overview**

This script demonstrates how to compute and interpret Receiver Operating Characteristic (ROC) curves and Area Under the ROC Curve (AUROC) scores using Random Forest and Naive Bayes classifiers. Below is the step-by-step breakdown:
## **Script Flow**

- **Generate Synthetic Dataset**  
  - Creates a binary classification dataset with 2,000 samples and 10 features.  
  - Simulates a realistic classification problem.

- **Add Noisy Features**  
  - Appends random, irrelevant features to increase the dataset's complexity.  
  - Mimics challenging real-world scenarios where not all features are informative.

- **Split the Data**  
  - Divides the dataset into training (80%) and testing (20%) subsets.  
  - Ensures unbiased model evaluation on unseen data.

- **Train Classification Models**  
  - Builds two models:  
    - **Random Forest**: A robust ensemble-based classifier.  
    - **Naive Bayes**: A simple probabilistic model based on Bayes' theorem.

- **Generate Prediction Probabilities**  
  - Computes predicted probabilities for each class.  
  - Retains probabilities for the positive class to construct the ROC curve.

- **Compute AUROC and ROC Curve Values**  
  - Calculates:  
    - **AUROC**: Measures model performance (higher is better).  
    - **ROC Values**: False Positive Rate (FPR) and True Positive Rate (TPR) across thresholds.

- **Visualize ROC Curve**  
  - Plots FPR (x-axis) against TPR (y-axis) for each model.  
  - Includes AUROC scores in the legend for comparison.
## **Key Outputs**
- **AUROC Scores**  
  - Evaluates the overall discriminative power of the classifiers.  

- **ROC Plot**  
  - Visualizes how well each model distinguishes between positive and negative classes across thresholds.  
  - A random prediction baseline is included for reference.
## **Conclusion**
This script illustrates the process of building, evaluating, and visualizing classification models using ROC curves. It highlights the strengths and weaknesses of different models in distinguishing classes.

# Output

### Interpretation of the Script Output

- **Random (Chance) Prediction: AUROC = 0.500**
    - An AUROC score of **0.500** represents a random guessing model with no predictive power.
    - The model's True Positive Rate (TPR) is equal to its False Positive Rate (FPR) across all thresholds, resulting in a diagonal line on the ROC curve.
    
- **Random Forest: AUROC = 0.922**
    - An AUROC score of **0.922** indicates excellent model performance.
    - The Random Forest classifier has a high ability to distinguish between positive and negative classes, with a much higher TPR than FPR across thresholds.
- 
- **Naive Bayes: AUROC = 0.993**
    - An AUROC score of **0.993** suggests near-perfect model performance.
    - The Naive Bayes classifier has an extremely high discriminative power, with TPR approaching 1 and FPR close to 0 for most thresholds.

### Summary

- The **Naive Bayes classifier** outperforms the **Random Forest classifier** in this specific setup.
- Both models significantly outperform random guessing (baseline AUROC = 0.500), indicating their utility for this classification task.
- However, such high performance (especially for Naive Bayes) may suggest that the dataset or features are particularly well-suited to the model, or there may be minimal noise in the classification task. Further evaluation (e.g., on new datasets) is recommended to confirm robustness.