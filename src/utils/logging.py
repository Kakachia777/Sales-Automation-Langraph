import logging
import sys
from datetime import datetime
from pathlib import Path

class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Create logs directory if it doesn't exist
        Path("logs").mkdir(exist_ok=True)
        
        # File handler
        file_handler = logging.FileHandler(
            f"logs/outreach_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message: str):
        self.logger.info(message)
    
    def error(self, message: str):
        self.logger.error(message)
    
    def warning(self, message: str):
        self.logger.warning(message) 