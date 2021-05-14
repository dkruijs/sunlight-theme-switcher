Gnome 3 daylight dark/light theme switcher
---

### Setting up 
Create a recurring anacron job as follows (by adding it to `/etc/cron.{daily|weekly|monthly}`): 
```
# period delay job-identifier command
3 5 daylight-theme-switcher python -c 'from theme_switcher import update_sunrise_sunset; update_sunrise_sunset()'
```
(or use some custom cron job if desired)

### How it works
This job will periodically update your crontab with a job that automatically switches dark and light themes depending on sunrise/sunset times, such as the following example:
```
# m h dom mon dow user  command
45 5 * * 0 python -c 'from theme_switcher import set_light_theme; set_light_theme()'  # sunrise @ 05:45
28 21 * * 0 python -c 'from theme_switcher import set_dark_theme; set_dark_theme()'  # sunset @ 21:28
```
Using only pure python and GTK commands. Tested on Ubuntu 20.04.2 LTS with GNOME 3 desktop version 3.36.8.