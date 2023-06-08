import logging
from src.date_format import currentdate_str

file_name = f"my_log_{currentdate_str}.log"
file_path_name = f"/Users/demon/Documents/PycharmProjects/CRMbanking/logs/my_log_{currentdate_str}.log"
logging.basicConfig(
    filename=file_name, encoding='utf-8',
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.DEBUG
)
logger = logging.getLogger()

# logger.error("Hello from ERROR")
# logger.warning("Hello from WARNING")
# logger.info("Hello from INFO")
# logger.debug("Hello from DEBUG")
