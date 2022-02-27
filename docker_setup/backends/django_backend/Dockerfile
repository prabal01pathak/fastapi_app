FROM multi_backend_backends
RUN cd /app/backend/django_backend/testing/
EXPOSE 8000
RUN ["python","/app/backend/django_backend/testing/manage.py","makemigrations"]
RUN ["python","/app/backend/django_backend/testing/manage.py","migrate"]
CMD ["python","/app/backend/django_backend/testing/manage.py","runserver"]