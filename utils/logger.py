import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logger(experiment_name: str, log_dir: str = "../logs", log_level: str = "INFO", max_bytes: int = 5*1024*1024, backup_count: int = 5) -> logging.Logger:
    """
    Sets up a logger with file and console handlers for logging training and evaluation processes.
    
    Parameters:
    - experiment_name (str): Name of the experiment for log file naming.
    - log_dir (str): Directory where log files are saved.
    - log_level (str): Logging level (e.g., "INFO", "DEBUG").
    - max_bytes (int): Max size of a log file in bytes before rotation (default: 5 MB).
    - backup_count (int): Number of backup files to keep (default: 5).
    
    Returns:
    - logger (logging.Logger): Configured logger instance.
    """
    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Log file path with timestamp and experiment name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"{experiment_name}_{timestamp}.log")

    # Create logger
    logger = logging.getLogger(experiment_name)
    logger.setLevel(log_level.upper())

    # Set up console handler for real-time monitoring
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())
    console_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_format)
    
    # Set up file handler with rotation for long-running experiments
    file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_format)
    file_handler.setLevel(log_level.upper())

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Starting log message
    logger.info(f"Logger initialized for experiment: {experiment_name}")
    
    return logger
