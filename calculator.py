import time
import logging
import day8_db as p
import re

def add(message,logger_info):
    Values=message.split("+")
    try:
        result=(int(Values[0])+int(Values[1]))
        logger_info.info('{}={}'.format((message),(result)))
        return int(result)

    except ValueError:
       logger_info.warning("{},values can not be alphabet".format(message))
       return "alphabet can not be operated"

def sub(message,logger_info):
    Values=message.split("-")
    try:
        result=int(Values[0])-int(Values[1])
        logger_info.info('{}={}'.format((message),(result)))
        return result

    except ValueError:

        logger_info.warning("{},operant should be integar".format(message))
        return "alphabet can not be operated"

def multiply(message,logger_info):
    Values=message.split("*")
    try:
        result=int(Values[0])*int(Values[1])
        logger_info.info('{}={}'.format((message),(result)))
        return result
    except ValueError:
        logger_info.exception("{},operant should be integar".format(message))
        return "alphabet can not be operated"

def div(message,logger_info):
    Values=message.split("/")
    try:
        result=int(Values[0])/int(Values[1])
        logger_info.info('{}={}'.format((message),(result)))
        return result
    except ValueError:
        logger_info.warning("{},operant should be integar".format(message))
        return "alphabet can not be operated"
    except ZeroDivisionError:
        logger_info.warning("{},value can not be divided by zero".format(message))
        return "divisior can not  be zero"


class LogDBHandler(logging.Handler):


    def __init__(self):
        logging.Handler.__init__(self)
        self.sql_cursor = p.c
        self.sql_conn = p.conn

    def emit(self, record):
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created))

        #self.log_msg = record.msg
        #self.log_msg = self.log_msg.strip()
        #self.log_msg = self.log_msg.replace('\'', '\'\'')
        sql = 'INSERT INTO calci_db5(OPERATOR_EXPRESSION,DATE_TIME) VALUES(' + \
            '\''   + record.msg + '\', '+ \
            '\'' + str(tm) + '\');'
        p.data_show_db5()
        #p.data_entry(sql)
        self.sql_cursor.execute(sql)
        print(sql)
        p.data_compare()
        return sql


if __name__ == "__main__":

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    fh = LogDBHandler()
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(msg)s %(asctime)s")
    #print(vars(formatter))
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    logger.addHandler(ch)
    logger.addHandler(fh)



    opreator_string=input("perform operation")
    if "+" in opreator_string:
        add(opreator_string,logger)

    elif "-" in opreator_string:
        sub(opreator_string,logger)
    elif "*" in opreator_string:
        multiply(opreator_string,logger)
    elif "/" in opreator_string:
        div(opreator_string,logger)
    else:
        logger.warning("{},operation unrecognised".format(opreator_string))
