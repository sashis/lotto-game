FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
COPY dist/*.whl .
RUN pip install *.whl
ENTRYPOINT ["lotto"]
