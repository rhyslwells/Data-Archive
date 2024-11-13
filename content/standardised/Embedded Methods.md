Embedded methods for [[Feature Selection]] ==integrate feature selection directly into the model training process.==

Embedded methods provide a convenient and efficient approach to feature selection by seamlessly integrating it into the model training process, ultimately leading to models that are more parsimonious and potentially more interpretable.

1. **Incorporated into Model Training**: Unlike [[Filter method]] and [[Wrapper Methods]], which involve feature selection as a separate step from model training, embedded methods perform feature selection simultaneously with model training. This means that feature importance or relevance is determined within the context of the model itself.

2. **Regularization Techniques**: Embedded methods commonly use [[Regularisation]] techniques to penalize the inclusion of unnecessary features during model training. 

3. **Automatic Feature Selection**: Embedded methods automatically select the most relevant features by learning feature importance during the training process. The model adjusts the importance of features iteratively based on their contribution to minimizing the [[Loss function]].

4. **Examples of Embedded Methods**:
   - **[[Lasso]] (L1 Regularization)**:
   - [[Elastic Net]]: Elastic Net combines L1 ([[Lasso]]) and L2 ([[Ridge]]) regularization .
   - **Tree-based Methods**: [[Decision Tree]] and ensemble methods like [[Random Forests]] and [[Gradient Boosting]] inherently perform feature selection during training by selecting the most informative features at each split node of the tree.

5. **Advantages**:
   - Simplicity: Embedded methods simplify the feature selection process by integrating it into model training, reducing the need for additional preprocessing steps.
   - Efficiency: Because feature selection is performed during model training, embedded methods can be more computationally efficient compared to wrapper methods, which require training multiple models.

6. **Considerations**:
   - Hyperparameter Tuning: Tuning regularization parameters or other model-specific parameters may be necessary to optimize feature selection performance.
   - Model [[interpretability]]: While embedded methods can automatically select features, interpreting the resulting model may be challenging, especially for complex models like ensemble methods.

