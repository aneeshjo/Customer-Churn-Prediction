import logging
import os
from datetime import datetime
from pathlib import Path


# ==========================================================
# Create Log File Name
# ==========================================================
LOG_FILE_NAME = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# ==========================================================
# Create Log Directory
# ==========================================================
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

# ==========================================================
# Create Log File Path
# ==========================================================
LOG_FILE_PATH = LOG_DIR / LOG_FILE_NAME

# ==========================================================
# Configure Logger
# ==========================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)