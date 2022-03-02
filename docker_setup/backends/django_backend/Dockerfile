FROM multi_backend_backends
WORKDIR /app/backend/django_backend/testing/
RUN ["python","manage.py","makemigrations"]
RUN ["python","manage.py","migrate"]
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=8", "testing.wsgi"]