FROM multi_backend_backends
RUN ["python","/app/backend/django_backend/testing/manage.py","makemigrations"]
RUN ["python","/app/backend/django_backend/testing/manage.py","migrate"]
CMD ["python","/app/backend/django_backend/testing/manage.py","runserver","0.0.0.0:8000"]