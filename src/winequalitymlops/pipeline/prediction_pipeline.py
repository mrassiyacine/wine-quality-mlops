import joblib
import numpy as np
from pathlib import Path

class PredictionPipeline:
    def __init__(self) -> None:
        self.model_path: Path = Path('artifacts/model_trainer/model.joblib')
        self.model = joblib.load(self.model_path)

    def predict(self, data: np.ndarray) -> np.ndarray:
        prediction: np.ndarray = self.model.predict(data)
        return prediction