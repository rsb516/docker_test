
# Use the official Python image as the build image
FROM python:3.9

WORKDIR /src

COPY iris_classification.py requirements.txt/ .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["python", "iris_classification.py"]