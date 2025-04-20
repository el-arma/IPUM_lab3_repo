import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import joblib


def train_model():
    # 1. Load the Iris dataset
    iris = datasets.load_iris()
    X = iris.data  # Features
    y = iris.target  # Labels

    # 2. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    # 3. Train SVM (RBF kernel)
    svm_clf = SVC(kernel="rbf", C=1.0, gamma="scale")
    svm_clf.fit(X_train, y_train)

    # 4. Predict and evaluate
    y_pred = svm_clf.predict(X_test)

    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))

    # 5. Visualize with PCA (2D projection)
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_train)

    plt.figure(figsize=(8, 6))

    for _, label in enumerate(np.unique(y_train)):
        plt.scatter(
            X_pca[y_train == label, 0],
            X_pca[y_train == label, 1],
            label=iris.target_names[label],
        )

    plt.title("Iris Dataset (PCA projection)")
    plt.legend()
    plt.grid(True)
    plt.show()

    return svm_clf


def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")


if __name__ == "__main__":
    rdy_model = train_model()
    save_model(rdy_model, "svm_iris_model_v1.joblib")
