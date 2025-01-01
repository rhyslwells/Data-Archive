---
tags:
  - ml_optimisation
  - evaluation
---
[[Model Building]]
- Pick a model
- Develop and implement algorithms that can predict outcomes based on the selected features.
- Do not think about refinement yet.
- [[parametric vs non-parametric models]] &     [[Determining the right algorithm]]

# Setting Up Training and Test Sets

Train the model using the prepared data to learn patterns and make predictions.

The model is trained on your dataset, which is typically divided into three main subsets: training, development (dev), and test sets.
### Purpose of Each Set

- **Training Set**: Used to fit the model. This is where the model learns the patterns and relationships within the data. The majority of the data is allocated here to ensure the model has enough information to learn effectively.
- **Development (Dev) Set**: Also known as the validation set, it is used to tune the model's parameters and make decisions about model architecture. It helps in preventing overfitting by providing a separate dataset to evaluate the model's performance during training.
- **Test Set**: Used to evaluate the final model's performance. This set is not used during the training process and provides an unbiased evaluation of the model's ability to generalize to new, unseen data.

Historical Suggestions
- **Train-Test Sets**: 70% training, 30% testing.
- **Train-Dev-Test**: 60% training, 20% development, 20% testing.

Modern Approach
- With larger datasets, a split of 98% training, 1% development, and 1% testing is often used. This is because modern models require more data to learn effectively, and larger datasets allow for smaller proportions to be allocated to dev and test sets while still maintaining sufficient data for evaluation.

Code Example
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3)
```
Considerations
- **Data Setup**: Be careful when setting up the training and test data to ensure they are ==representative== of the problem domain.
- ==**Distribution**: Dev and test sets should be from the same distribution to ensure consistent evaluation metrics. Avoid having subsets that are biased, such as data from the same geographical area.==
- **Random Shuffling**: Randomly shuffle the data before splitting to ensure that each subset is representative of the whole dataset.
- **Cross-Validation**: Consider using cross-validation techniques to make the most of your data, especially when the dataset is small.

## Handling Different Distributions

Video Resource
- [Training and Testing on Different Distributions](https://www.youtube.com/watch?v=sfk5h0yC67o&list=PLkDaE6sCZn6E7jZ9sN_xHwSHOdjUxUW_b&index=16)

Example
- High-resolution photos (many) vs. amateur photos (small number). These have different distributions.

Strategy
- Combine and randomly shuffle into train-dev-test sets.
- Use the dev set to guide model tuning and target setting.
- Best practice is to train using the larger, more diverse cases and validate with the specific cases you are interested in.
- Ensure the dev set is aligned with your goals to achieve the desired model performance.


