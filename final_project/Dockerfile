FROM python:3

WORKDIR /app

COPY . /app/
RUN pip install -r django_requirements.txt

EXPOSE 8000

ENTRYPOINT "./server_startup.sh"
