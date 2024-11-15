import os
import matplotlib.pyplot as plt
from datetime import datetime

def save_plot(fig: plt.Figure, output_dir: str, experiment_name: str, plot_name: str) -> str:
    """
    Saves a matplotlib figure to the specified directory as a PNG image.

    Parameters:
    - fig (plt.Figure): Matplotlib figure object to be saved.
    - output_dir (str): Directory where the plot will be saved.
    - experiment_name (str): Name of the experiment, used in the filename.
    - plot_name (str): Name of the plot (e.g., "loss_curve").

    Returns:
    - plot_path (str): Path where the plot was saved.
    """
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{experiment_name}_{plot_name}_{timestamp}.png"
    plot_path = os.path.join(output_dir, filename)
    fig.savefig(plot_path)
    plt.close(fig)  # Close the figure after saving to free memory
    print(f"Plot saved to {plot_path}")
    return plot_path
