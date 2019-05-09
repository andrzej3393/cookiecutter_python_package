FROM python:3.7
ENV PYTHONUNBUFFERED 1
COPY requirements/concrete/requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY dist/*.whl .
RUN python3 -m pip install *.whl
