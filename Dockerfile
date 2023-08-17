from python3.8

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt


CMD [ "./src/main.py" ]