FROM python

WORKDIR /opt/

COPY . /opt/

RUN pip install -r requirements.pip

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]