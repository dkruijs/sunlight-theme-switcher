Gnome 3 daylight dark/light theme switcher
---

***Work in progress***

This package is meant to be run as a cron job, and will change required settings in Gnome 3 based on regularly updated sunrise/sunset times. Updated times are calculated off-line by the `astral` package.

### Setting up 
Create a weekly cron job as follows (with the specified time and frequency you desire): 
```
0 11 * * 0
python -c 'from theme_switcher import update_sunrise_sunset; update_sunrise_sunset()'
```
This function will retrieve updated sunrise and sunset times, and use this data to insert (on the first run) or update (on subsequent runs) your crontab with a cron job for switching the user-configured 'light mode' and 'dark mode' settings automatically, by default at sunrise and sunset. 

You can set a desired relative delta in your config file in hours and minutes if you prefer to trigger the settings changes earlier or later.

Set up location information (based on `astral`'s requirements) in an `.env` file in your root folder as such:
```
CITY='Amsterdam'
COUNTRY='Netherlands'
TIMEZONE='Europe/Amsterdam'
LATITUDE='52.4'
LONGITUDE='-4.9'
```

### Installation
_Coming soon._