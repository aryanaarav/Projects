# K-Nearest Neighbors (KNN) Algorithm

This project demonstrates the implementation and evaluation of the K-Nearest Neighbors (KNN) algorithm for supervised machine learning.

## Overview

K-Nearest Neighbors is a simple, non-parametric, and lazy learning algorithm used for both classification and regression. In this project, KNN is used for classification tasks, with hyperparameter tuning via GridSearchCV to find the best-performing model.

## Implementation Details

- **Algorithm:** KNeighborsClassifier from `scikit-learn`
- **Hyperparameter Tuning:** Performed using `GridSearchCV`
- **Parameters Tuned:**
  - `n_neighbors`: Number of neighbors (1 to 10)
  - `algorithm`: ['auto', 'ball_tree', 'kd_tree', 'brute']
  - `p`: Power parameter for Minkowski metric (1 or 2)
- **Validation:** 10-fold cross-validation (`cv=10`)
- **Evaluation:** The best parameters and model accuracy are reported on both training and test sets.

## Sample Usage

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

parameters = {
    'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
    'p': [1, 2]
}

KNN = KNeighborsClassifier()
knn_cv = GridSearchCV(KNN, parameters, cv=10)
knn_cv.fit(X_train, Y_train)

print("Tuned hyperparameters (best parameters):", knn_cv.best_params_)
print("Accuracy:", knn_cv.best_score_)
```

To evaluate the model on test data:
```python
test_accuracy = knn_cv.score(X_test, Y_test)
print("Test set accuracy:", test_accuracy)
```

## Results

- The best parameters found in this project were typically:
  - `algorithm`: 'auto'
  - `n_neighbors`: 10
  - `p`: 1
- Achieved cross-validation accuracy: ~0.85 (exact value may vary per run and dataset)
- The model's accuracy was also calculated on the test set for final evaluation.

## File Location

The relevant code and implementation are found in:
- `DataScienceProjects/Supervised Learning/Classification Algorithms/KNN/KNNalgorithm.ipynb`

## References

- [scikit-learn KNeighborsClassifier Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [scikit-learn GridSearchCV Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

---

*Note: This README is based on the code and approach found in the notebook. For more details, see the code in the referenced notebook file.*

---

For more examples or to see the code in context, you can view the full notebook and repository on [GitHub](https://github.com/aryanaarav/Projects/search?q=knn).
