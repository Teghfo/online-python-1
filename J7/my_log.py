import logging

path = 'log/login.log'

logging.basicConfig(format="[ %(asctime)s ]: %(levelname)s: path: %(filename)s [%(funcName)s] line_number: %(lineno)d - message: %(message)s",
                    datefmt="%Y:%m:%d - %H:%M" ,filename=path ,level='DEBUG')




def greeting():
    logging.info('info')


logging.debug('debug')
logging.error('error')
logging.critical('critical')
logging.warning('warning')
greeting()