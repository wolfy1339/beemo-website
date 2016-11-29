FROM python:3
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ADD . /
EXPOSE 8080

CMD ["python", "run.py"]
