"""
Training script for Parkinson's disease screening CNN
"""

import numpy as np
from cnn_model import build_cnn_model

def train_model(X_train, y_train, X_val, y_val):
    """
    Train CNN model using prepared datasets.
    """

    model = build_cnn_model()

    history = model.fit(
        X_train,
        y_train,
        validation_data=(X_val, y_val),
        epochs=20,
        batch_size=32
    )

    return model, history


if __name__ == "__main__":
    print("Training pipeline defined.")
    print("Load dataset externally and call train_model().")
