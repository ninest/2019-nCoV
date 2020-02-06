import requests
import json
import datetime

from secrets import API_KEY  # use env later


SPREADSHEET_ID = "1UF2pSkFTURko2OvfHWWlFpDFAr1UxCBA4JLwlSP6KFo"
url = lambda sheet : f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{sheet}?key={API_KEY}"

class NCOVData:
  def __init__(self):
    pass

  def get_sheet_data(self, sheet_url):  
    response = requests.get(sheet_url)
    if response.status_code == 200:
      return json.loads(response.content)
  

  def get_data(self, sheet_url, country=None): # only gets data for either confirmed, deaths, or recovered
    content = self.get_sheet_data(sheet_url)

    all_places = []
    dates = []
    for date in content['values'][0][5:]:
      # 1/21/2020 10:00 PM	
      date_obj = datetime.datetime.strptime(date, '%m/%d/%Y %I:%M %p')
      dates.append(date_obj)

    for data in content['values'][1:]:
      province_state = data[0]
      country_region = data[1]
      coords = {'lat': data[3], 'lon': data[4]}

      cases = []
      # cases = [data[5:]
      for c in data[5:]:
        try: cases.append(int(c))
        except: cases.append(0)

      if cases == []:
        # no cases, so just set to list of 0s
        cases = [0] * len(dates)
        

      all_places.append({
        'province_state': province_state,
        'country_region': country_region,
        'coords': coords,
        'dates': dates,  # maybe don't need to put here?
        'cases': cases
      })
    
    if country == None:
      return all_places
    else:
      filtered_all_places = [place for place in all_places if place['country_region'] == country]
      return filtered_all_places[0]
    
  
  def get_all_country_data(self, country):
    confirmed = self.get_data(url('Confirmed'), country)
    recovered = self.get_data(url('Recovered'), country)
    death = self.get_data(url('Death'), country)

    return {
      'confirmed': confirmed,
      'recovered': recovered,
      'death': death,
    }
