FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
WORKDIR /lotto-game
COPY . /lotto-game
RUN pip install .
ENTRYPOINT ["lotto"]
