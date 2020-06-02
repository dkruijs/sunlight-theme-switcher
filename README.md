Gnome 3 daylight dark/light theme switcher
---

### Setting up 
Create a weekly cron job as follows: 
```
0 11 * * 0
python -c 'from theme_switcher import update_sunrise_sunset; update_sunrise_sunset()'
```
This function will retrieve updated sunrise and sunset times, and use this data to insert (on the first run) or update (on subsequent runs) your crontab with a cron job for switching the user-configured 'light mode' and 'dark mode' settings automatically, by default at sunrise and sunset. 

You can set a desired relative delta in your config file in hours and minutes if you prefer to trigger the settings changes earlier or later.

### Installation
_Coming soon._