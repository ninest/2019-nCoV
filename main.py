from matplotlib import pyplot as plt, dates as mdates
import numpy as np

from ncov_data import url, NCOVData

ncov_data = NCOVData()
singapore_data = ncov_data.get_all_country_data('Singapore')

dates = singapore_data['confirmed']['dates']  # same for all

confirmed = singapore_data['confirmed']['cases']
recovered = singapore_data['recovered']['cases']
death = singapore_data['death']['cases']



# all the lenghts should be the same
length = len(confirmed)
print(length)

if len(recovered) != length:
  for i in range(length - len(recovered)):
    recovered.append(None)
if len(death) != length:
  for i in range(length - len(death)):
    death.append(None)
print(len(death))

# # convert dates to matplotlib dates
dates = [mdates.date2num(d) for d in dates]

# format dates correctyl and nicely
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))

# interval so graph is not cluttered
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))


plt.plot(dates, confirmed,  label='Confirmed cases')

# possibility of deaths and recovers to be empty
try: plt.plot(dates, death,  label='Death cases')
except: print("No deaths")

try: plt.plot(dates, recovered,  label='Recovered cases')
except: print("No recoveries")

plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('2019-nCoV Singapore')

# # # make the dates slant
plt.gcf().autofmt_xdate()

# plt.scale("log")
plt.legend()
plt.show()
