FROM alpine:3.5
RUN apk add --update py2-pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
COPY templates/index.html .
COPY main.py .
COPY templates/index.html /templates/
EXPOSE 5000
CMD ["python", "main.py"]