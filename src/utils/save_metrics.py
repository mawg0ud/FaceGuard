import os
import json
from typing import Dict
from datetime import datetime

def save_metrics(metrics: Dict[str, float], output_dir: str, experiment_name: str, epoch: int = None) -> str:
    """
    Saves experiment metrics to a JSON file.

    Parameters:
    - metrics (dict): Dictionary of metric names and values.
    - output_dir (str): Directory where metrics will be saved.
    - experiment_name (str): Name of the experiment, used in the filename.
    - epoch (int, optional): Epoch number to save metrics for checkpoint tracking.

    Returns:
    - metrics_path (str): The path where the metrics file was saved.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{experiment_name}_metrics"
    if epoch is not None:
        filename += f"_epoch{epoch}"
    filename += f"_{timestamp}.json"
    metrics_path = os.path.join(output_dir, filename)
    with open(metrics_path, 'w') as file:
        json.dump(metrics, file, indent=4)
    print(f"Metrics saved to {metrics_path}")
    return metrics_path
