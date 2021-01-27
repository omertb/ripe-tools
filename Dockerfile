FROM python:latest

WORKDIR /project
COPY ./requirements.txt requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "--chdir", "/project", "run:app", "--reload", "--timeout", "900"]