FROM multi_backend_backends
WORKDIR /app/backend/flask_backend/
ENV FLASK_APP=main 
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers=8", "main:app"]