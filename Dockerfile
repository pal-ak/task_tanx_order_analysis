# using Python as a parent image
FROM python:3.9-slim

# setting the working directory in the container
WORKDIR /app

# copying the current directory contents into the container at /app
COPY . /app

# install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# run app.py when container launches
CMD ["python", "app.py"]
