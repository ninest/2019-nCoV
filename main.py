from matplotlib import pyplot as plt, dates as mdates
import numpy as np

from ncov_data import url, NCOVData

def produce_chart(country=None, state=None, log=False):
  if country == None and state == None:
    raise Exception('No place/region provided')

  ncov_data = NCOVData()
  place_data = ncov_data.get_all_country_data(country=country, state=state)

  dates = place_data['confirmed']['dates']  # same for all

  confirmed = place_data['confirmed']['cases']
  recovered = place_data['recovered']['cases']
  death = place_data['death']['cases']

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

  if state:
    place_title = f'{state}, {country}'
  else:
    place_title = country
  plt.title(f'2019-nCoV {place_title}')

  # # # make the dates slant
  plt.gcf().autofmt_xdate()

  if log: plt.yscale("log")

  plt.legend()

  plt.tight_layout()

  # plt.show()

  if state:
    save_name = f"{country.replace(' ', '_')}-{state.replace(' ', '_')}"
    if log: save_name += '-log'
  else:
    save_name = f"{country.replace(' ', '_')}"

  plt.savefig(f'charts/{save_name}.png')

  # reset plot
  plt.cla()
  plt.clf()

  print(country)

produce_chart(country='Singapore')
produce_chart(country='Japan')
produce_chart(country='Mainland China', state='Hubei')
produce_chart(country='Mainland China', state='Hubei', log=True)