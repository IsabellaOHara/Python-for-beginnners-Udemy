import logging

logging.basicConfig(filename="mylog.log", level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warning("warning") # default
logging.info("info")
logging.debug("debug")

