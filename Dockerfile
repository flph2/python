FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY mysite /app/
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000
