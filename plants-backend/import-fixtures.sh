#!/bin/sh

# To dump a file from the ddbb
# python manage.py dumpdata apiapp.User --indent 4 > users.json
python manage.py loaddata users
python manage.py loaddata presets
python manage.py loaddata plants
python manage.py loaddata arduinos
python manage.py loaddata user2plantation
python manage.py loaddata plantation2arduino
python manage.py loaddata measurements
python manage.py loaddata avg_measurement

