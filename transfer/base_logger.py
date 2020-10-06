from loguru import logger
logger.add("debug.log", format="{level} {message}", rotation="10 KB", level="DEBUG")
