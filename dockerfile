# using python as the base image 
FROM python:3.11-slim 

# defining the work directory
WORKDIR /app

# copying the requirements to the work directory
COPY requirements.txt .

# install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the app code to the work directory
COPY . .

# set the app port
EXPOSE 8000

# the parameters to run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
