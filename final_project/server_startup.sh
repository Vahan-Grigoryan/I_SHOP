python manage.py migrate;
python manage.py shell <<EOF
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
EOF

python manage.py loaddata dumped_sqlite.json;


python manage.py runserver 0.0.0.0:8000;
