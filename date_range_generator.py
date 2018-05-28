from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

six_months = relativedelta(months=+3)
start_date = date(2005, 1, 1)
end_date = start_date + six_months
today = date.today()
formatter = '%d-%m-%Y' 

with open('dates.txt', 'w') as date_file:
	while end_date < today:
		start_formatted = datetime.strftime(start_date, formatter)
		end_formatted = datetime.strftime(end_date, formatter)
		logger.info('{} to {}'.format(start_formatted, end_formatted))
		date_file.write('{},{}\n'.format(start_formatted, end_formatted))
		start_date = end_date + timedelta(days=1)
		end_date = start_date + six_months
	start_formatted = datetime.strftime(start_date, formatter)
	end_formatted = datetime.strftime(today, formatter)
	logger.info('{} to {}'.format(start_formatted, end_formatted))
	date_file.write('{},{}\n'.format(start_formatted, end_formatted))

