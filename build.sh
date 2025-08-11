set -e

pip install -r requirements.txt

python manage.py collectstaton --on-input
python manage.py migrate