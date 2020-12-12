FROM python:latest
WORKDIR /app
COPY . .
RUN pip3 install paho-mqtt
CMD ["python3", "main-mdms.py"]