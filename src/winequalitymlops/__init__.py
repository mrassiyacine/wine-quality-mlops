import logging
import os
import sys

logging_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(os.path.join(log_dir, "running_logs.log"), mode="w"),
    ],
)
logger = logging.getLogger("wine-quality-mlops")
