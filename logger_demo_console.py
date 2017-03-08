import logging

class LoggerDemoConsole():
# https://docs.python.org/2/howto/logging-cookbook.html#multiple-handlers-and-formatters

    def testLog(self):

        #create logger
        logger = logging.getLogger(LoggerDemoConsole.__name__) # ___name__ strips functionality off methods and turns them into strings
        logger.setLevel(logging.INFO) # set the base level of logging

        #create console handler and set level to info
        chandler = logging.StreamHandler() #StreamHandler is one of many log handlers, in this case, allowing us to move logs to other places
        chandler.setLevel(logging.INFO)

        #create formatter
        formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        #add formatter to console handler -> ch
        chandler.setFormatter(formatter)

        #add console handler to logger
        logger.addHandler(chandler)

        #logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical messsage')

demo = LoggerDemoConsole()
demo.testLog()
