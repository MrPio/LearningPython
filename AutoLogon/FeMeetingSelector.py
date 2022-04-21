import datetime
import webbrowser

import AutoLogonRun

AutoLogonRun.perform_login()
weekday = datetime.datetime.today().weekday()
url = ''
if weekday == 2:
    url = 'https://learn.univpm.it/mod/url/view.php?id=295745'
elif weekday == 3:
    url = 'https://learn.univpm.it/mod/url/view.php?id=295746'
elif weekday == 4:
    url = 'https://learn.univpm.it/mod/url/view.php?id=295747'
else:
    exit(0)
webbrowser.open(url, new=2)
