FROM python:3.9.0

WORKDIR /app/

COPY . /app/

RUN python3 -m venv myvenv && . myvenv/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]