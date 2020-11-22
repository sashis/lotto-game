FROM python:3.9-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /lotto-game
COPY . .
RUN pip install .
ENTRYPOINT ["lotto"]
