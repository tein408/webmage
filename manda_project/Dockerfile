FROM python:3.9.0

WORKDIR /app/

COPY requirements.txt /app/

COPY . /app/

RUN python -m venv myvenv && . myvenv/bin/activate && pip install -r requirements.txt

EXPOSE 8000

CMD ["./myvenv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
