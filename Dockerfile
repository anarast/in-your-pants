FROM python:3.8

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /pants
COPY . /pants

ENTRYPOINT ["python3"]

CMD ["in_your_pants.py"]
