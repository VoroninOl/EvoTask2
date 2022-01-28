FROM python 

WORKDIR /app

COPY . .

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4000

VOLUME [ "/app/database" ]

CMD ["python", "main.py"]