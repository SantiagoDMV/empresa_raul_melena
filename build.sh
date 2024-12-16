#1/usr/bin/env bash 

set -o errexit

pip install -r requirements.txt

python manage.py collectstaic --noinput
python manage.oy migrate