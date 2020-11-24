FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /lotto-game
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN pip install .
ENTRYPOINT ["lotto"]
