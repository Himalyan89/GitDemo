import logging

def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) # file handler object

    logger.setLevel(logging.CRITICAL)
    logger.debug("A debug statement is printed")
    logger.info("Information statement")
    logger.warning("A warning statement is printed")
    logger.error("Error statement is printed")
    logger.critical("Critical issue found")
