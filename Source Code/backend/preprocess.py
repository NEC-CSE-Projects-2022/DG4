import numpy as np

def preprocess_input(data: dict):
    """
    Convert frontend JSON into model-ready array
    """

    # Example expected inputs (you can change later)
    features = [
        float(data.get("age", 50)),
        float(data.get("tumor_size", 2.5)),
        float(data.get("lymph_nodes", 0)),
        float(data.get("grade", 2))
    ]

    return np.array(features).reshape(1, -1)