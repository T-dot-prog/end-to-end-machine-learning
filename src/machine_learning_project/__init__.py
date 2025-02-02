import logging
import sys
from pathlib import Path
from datetime import datetime
import json
from typing import Optional, Dict, Any

class MLLogger:
    """
    Custom logger for machine learning projects with additional ML-specific logging features.
    Supports both file and console logging with different log levels and formats.
    """
    def __init__(
        self,
        name: str,
        log_dir: str = "logs",
        console_level: int = logging.INFO,
        file_level: int = logging.DEBUG
    ):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        # Create logs directory if it doesn't exist
        log_path = Path(log_dir)
        log_path.mkdir(parents=True, exist_ok=True)
        
        # Create formatters
        console_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(console_level)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_handler = logging.FileHandler(
            filename=log_path / f"{name}_{timestamp}.log",
            mode='a'
        )
        file_handler.setLevel(file_level)
        file_handler.setFormatter(file_formatter)
        self.logger.addHandler(file_handler)
        
        # Metrics logging
        self.metrics_file = log_path / f"{name}_{timestamp}_metrics.jsonl"
    
    def debug(self, message: str):
        """Log debug message."""
        self.logger.debug(message)
    
    def info(self, message: str):
        """Log info message."""
        self.logger.info(message)
    
    def warning(self, message: str):
        """Log warning message."""
        self.logger.warning(message)
    
    def error(self, message: str):
        """Log error message."""
        self.logger.error(message)
    
    def log_metrics(self, metrics: Dict[str, Any], step: Optional[int] = None):
        """
        Log training/evaluation metrics to a separate JSONL file.
        
        Args:
            metrics: Dictionary of metric names and values
            step: Optional training step or epoch number
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "metrics": metrics
        }
        if step is not None:
            log_entry["step"] = step
            
        with open(self.metrics_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    
    def log_hyperparameters(self, hyperparams: Dict[str, Any]):
        """Log model hyperparameters."""
        self.info("Hyperparameters:")
        for param, value in hyperparams.items():
            self.info(f"  {param}: {value}")
