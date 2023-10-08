FROM python

RUN pip install django

COPY . /opt/

WORKDIR /opt/mysite/

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]