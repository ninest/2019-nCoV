from matplotlib import pyplot as plt, dates as mdates
import numpy as np

from ncov_data import url, NCOVData

ncov_data = NCOVData()
# TODO: don't hardcode
singapore_data = ncov_data.get_all_country_data('Singapore')

dates = singapore_data['confirmed']['dates']  # same for all

confirmed = singapore_data['confirmed']['cases']
recovered = singapore_data['recovered']['cases']
death = singapore_data['death']['cases']

# # convert dates to matplotlib dates
dates = [mdates.date2num(d) for d in dates]

# style preset
# plt.xkcd()
# plt.style.use('fivethirtyeight')

# format dates correctyl and nicely %m/%d/%Y
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %-d, %-y'))

# interval so graph is not cluttered
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))

plt.plot(dates, death,  label='Death cases')
plt.plot(dates, recovered,  label='Recovered cases')
plt.plot(dates, confirmed,  label='Confirmed cases')

plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('2019-nCoV Singapore')

# # # make the dates slant
plt.gcf().autofmt_xdate()

# plt.yscale("log")
plt.legend()

plt.tight_layout()

# plt.show()
plt.savefig('fig.png')