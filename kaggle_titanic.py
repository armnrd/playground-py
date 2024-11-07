from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Load data
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Create and train the ensemble model
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    # Make predictions and evaluate
    y_pred = rf.predict(X_test)
    print(f'Random Forest Accuracy: {accuracy_score(y_test, y_pred)}')

if __name__ == "__main__":
    main()

