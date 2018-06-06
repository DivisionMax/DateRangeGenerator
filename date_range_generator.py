from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import argparse
from datetime import date, datetime
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

date_format = '%Y-%m-%d'
list_of_periods = ['weeks', 'months', 'days']

parser = argparse.ArgumentParser(description='Generate ranges of date from a given date, to a target date')
parser.add_argument('--period', dest='period', type=int,
                   help='The distance between generated periods')
parser.add_argument('--period_type', dest='period_type', help='The type of period to use when generating ranges', choices=list_of_periods)
parser.add_argument('--start', dest='start_date', help='The type of period to start generating date ranges from. Format: "2015-02-31"', default='2005-01-01', required=False, type=str)
parser.add_argument('--end', dest='end_date', help='The type of period to generate date ranges until. Format: "2015-02-31"', required=False, 
type=str, default=datetime.strftime(date.today(), date_format))

args = parser.parse_args()

start_date = datetime.strptime(args.start_date, date_format).date() 
final_date = datetime.strptime(args.end_date, date_format).date() 

if args.period_type == 'weeks':
	time_shift = relativedelta(weeks=args.period)
elif args.period_type == 'months':
	time_shift = relativedelta(months=args.period)
elif args.period_type == 'days':
	time_shift = relativedelta(days=args.period)
end_period_date = start_date + time_shift
output_format = '%d-%m-%Y' 

with open('dates.txt', 'w') as date_file:
	while end_period_date < final_date:
		start_formatted = datetime.strftime(start_date, output_format)
		end_formatted = datetime.strftime(end_period_date, output_format)
		logger.info('{} to {}'.format(start_formatted, end_formatted))
		date_file.write('{},{}\n'.format(start_formatted, end_formatted))
		start_date = end_period_date + timedelta(days=1)
		end_period_date = start_date + time_shift
	start_formatted = datetime.strftime(start_date, output_format)
	end_formatted = datetime.strftime(final_date, output_format)
	logger.info('{} to {}'.format(start_formatted, end_formatted))
	date_file.write('{},{}\n'.format(start_formatted, end_formatted))

