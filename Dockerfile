FROM python:3.11-alpine
WORKDIR /fotobog
COPY . .
RUN pip install --no-cache-dir -r requirements.txt 
CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000" ]