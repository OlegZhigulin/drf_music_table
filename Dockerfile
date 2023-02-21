FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN python3 music_api/manage.py makemigrations
RUN python3 music_api/manage.py migrate
CMD ["python", "music_api/manage.py", "runserver", "0.0.0.0:8000"]