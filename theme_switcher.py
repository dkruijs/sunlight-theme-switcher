#!/usr/bin/python

import os
import datetime
from crontab import CronTab

from astral import LocationInfo
from astral.sun import sun

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

def update_sunrise_sunset():
    city = LocationInfo(os.environ['CITY'], 
                        os.environ['COUNTRY'], 
                        os.environ['TIMEZONE'], 
                        os.environ['LATITUDE'], 
                        os.environ['LONGITUDE'])

    # Code block based on examples at https://astral.readthedocs.io/en/latest/index.html
    print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
    ))

    # Code block based on examples at https://astral.readthedocs.io/en/latest/index.html
    s = sun(city.observer, date=datetime.date.today())
    print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
    ))
