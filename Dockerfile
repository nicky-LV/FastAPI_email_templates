FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r ./requirements.txt
RUN pytest
RUN uvicorn run main:app --host 0.0.0.0 --port 8000 --reload

