import logging
import logging.config

class LoggerDemoConsole():
# https://docs.python.org/2/howto/logging-cookbook.html#multiple-handlers-and-formatters

    def testLog(self):

        #create logger
        logging.config.fileConfig('logging.conf') # allows us to fileConfig directly from a config file, like a Dockerfile build
        logger = logging.getLogger(LoggerDemoConsole.__name__) # ___name__ strips functionality off methods and turns them into strings
        
        #logging messages
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical messsage')

demo = LoggerDemoConsole()
demo.testLog()
