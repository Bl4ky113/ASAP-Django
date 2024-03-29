
import logging
from datetime import datetime

def request_error (name, exception):
    logger = logging.getLogger(name)

    print(exception)

    logger.warning(\
        'Request Error:\n\t' +\
        'type: ' + str('') 
    )

def critical_error (name, exception):
    logger = logging.getLogger(name)

    logger.critical(
        '\033[91mFATAL ERROR\033[0m: {};\n\ttype: {};\n\tmessage: {};\n\tat: {};\n\tfunction: {};\n\tline: {};'.format(
            datetime.utcnow(),
            type(exception).__name__,
            str(exception),
            exception.__traceback__.tb_frame.f_code.co_filename,
            exception.__traceback__.tb_frame.f_code.co_name,
            str(exception.__traceback__.tb_lineno)
        )
    )

    return
