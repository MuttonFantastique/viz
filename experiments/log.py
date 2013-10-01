import logging.config
import logging



logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

#error here: 
logging.config.fileConfig('/home/blackpanther/Desktop/sdlHacking/working/logging.txt')


#Module level logging
myLogger = logging.getLogger(__name__)
#python <2.6
disable_existing_loggers=False


myLogger.debug('hello')