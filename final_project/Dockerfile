FROM python:3

WORKDIR /app

COPY django_requirements.txt /app/
RUN pip install -r django_requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
