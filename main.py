from src.exception import InsuranceException
from src.logger import logging
import os
import sys
from src.utils import get_collection_as_dataframe


# def test_logger_and_expection():
#     try:
#        logging.info("Starting the test_logger_and_exception")
#        result = 3/0
#        print(result)
#        logging.info("Stoping the test_logger_and_exception")
#     except Exception as e:
#        logging.debug(str(e))
#        raise InsuranceException(e, sys)
    
if __name__=="__main__":
    try:
        get_collection_as_dataframe(database_name="INSURANCE", collection_name="INSURANCE_PROJECT")
        # test_logger_and_expection()
    except Exception as e:
        print(e)