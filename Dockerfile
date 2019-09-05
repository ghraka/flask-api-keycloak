FROM python:3.6
WORKDIR /usr/src/app
EXPOSE 5000

RUN pip install git+https://github.com/ghraka/flask-oidc
RUN pip freeze --local
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
