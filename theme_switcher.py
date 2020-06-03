#!/usr/bin/python

import os
import subprocess
import datetime

from crontab import CronTab
from astral import LocationInfo
from astral.sun import sun

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

#TODO: refactor to make an init function placing the original 'update' cron job 
# currently manually specified in README? 

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

    # Create a crontab object based on the user running this script:
    # Create crontab entry for switching to day-time settings
    # TODO: handle situations: 1. fresh crontab, 2. update earlier command, 3. remove all commands.
    with CronTab(user=True) as cron:
        job = cron.new(command="python -c 'from theme_switcher import set_day_settings; set_day_settings()'")
        job.hour.on(s['sunrise'].hour)
        job.minute.on(s['sunrise'].minute)

    # Create crontab entry for switching to night-time settings
    with CronTab(user=True) as cron:
        job = cron.new(command="python -c 'from theme_switcher import set_night_settings; set_night_settings()'")
        job.hour.on(s['sunset'].hour)
        job.minute.on(s['sunset'].minute)


# TODO: deal with other themes, settings (i.e. night light) via ENV variables
def set_day_settings():
    """Switches Gnome 3 settings to 'daylight' settings."""
    # TODO: refactor into 'execute process' wrapper function
    theme_process = subprocess.Popen(["gsettings", "set org.gnome.desktop.interface gtk-theme 'Adwaita'"],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    theme_stdout, theme_stderr = theme_process.communicate()

    nl_process = subprocess.Popen(["gsettings", "set org.gnome.settings-daemon.plugins.color night-light-enabled false"],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    nl_stdout, nl_stderr = nl_process.communicate()
    
    return theme_stdout, theme_stderr, nl_stdout, nl_stderr
    

def set_night_settings():
    """Switches Gnome 3 settings to 'night-time' settings."""
    theme_process = subprocess.Popen(["gsettings", "set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'"],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    theme_stdout, theme_stderr = theme_process.communicate()

    nl_process = subprocess.Popen(["gsettings", "set org.gnome.settings-daemon.plugins.color night-light-enabled true"],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    nl_stdout, nl_stderr = nl_process.communicate()

    return theme_stdout, theme_stderr, nl_stdout, nl_stderr