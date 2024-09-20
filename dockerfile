# using python as the base image 
FROM python:3.11-slim 

# defining the work directory
WORKDIR /app

# copying the requirements to the work directory
COPY requirements.txt .

# install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY wait-for-it.sh /app/

# Instalar curl (se necessário) para baixar o script
RUN apt-get update && apt-get install -y curl

RUN curl -o /usr/local/bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/local/bin/wait-for-it.sh

# copy the app code to the work directory
COPY . .

# set the app port
EXPOSE 8000

# the parameters to run the app
CMD ["./wait-for-it.sh", "postgres:5432", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]