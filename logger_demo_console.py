import logging

class LoggerDemoConsole():
# https://docs.python.org/2/howto/logging-cookbook.html#multiple-handlers-and-formatters

    def testLog(self):

        #create logger
        logger = logging.getLogger('sample_log')
        logger.setLevel(logging.INFO)

        #create console handler and set level to info
        chandler = logging,StreamHandler()
        chandler.setLevel(logging.ERROR)

        #create formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

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
