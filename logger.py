import logging

# Create logger
logger = logging.getLogger(__name__)

# Set default log level to DEBUG
logger.setLevel(logging.DEBUG)

# Create console handler and set its log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the console handler
formatter = logging.Formatter('%(asctime)s - pytest-bdd-demo - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add console handler to the logger
logger.addHandler(console_handler)
