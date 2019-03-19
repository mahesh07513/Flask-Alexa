import logging

class FirstClass(object):
	def __init__(self):
		self.current_number = 0
		self.logger = logging.getLogger(__name__)
		self.logger.setLevel(logging.WARNING)
		logger_handler = logging.FileHandler('python_logging.log')
		logger_handler.setLevel(logging.WARNING)
		logger_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		logger_handler.setFormatter(logger_formatter)
		self.logger.addHandler(logger_handler)
		self.logger.info('Completed configuring logger()!')
	def increment_number(self):
		self.current_number += 1
		self.logger.warning('Incrementing number!')
		self.logger.info('Still incrementing number!!')
	def decrement_number(self):
		self.current_number -= 1
	def clear_number(self):
		self.current_number = 0
		self.logger.warning('Clearing number!')
		self.logger.info('Still clearing number!!')
 
number = FirstClass()
number.increment_number()
number.increment_number()
print "Current number: %s" % str(number.current_number)
number.clear_number()
print "Current number: %s" % str(number.current_number)