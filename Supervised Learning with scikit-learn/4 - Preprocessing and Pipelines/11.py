# Create steps
steps = [
    ("imp_mean", SimpleImputer()), 
    ("scaler", StandardScaler()), 
    ("logreg", LogisticRegression())
]

# Set up pipeline
pipeline = Pipeline(steps)
params = {
    "logreg__solver": ["newton-cg", "saga", "lbfgs"],
    "logreg__C": np.linspace(0.001, 1.0, 10)
}

# Create the GridSearchCV object
tuning = GridSearchCV(pipeline, param_grid=params)
tuning.fit(X_train, y_train)
y_pred = tuning.predict(X_test)

# Compute and print performance
print(f"Tuned Logistic Regression Parameters: {tuning.best_params_}, Accuracy: {tuning.score(X_test, y_test)}")
