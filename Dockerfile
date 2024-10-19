# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install gcc and PostgreSQL client dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev curl

# Install pipenv
RUN curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Generate a new Pipfile.lock
RUN pipenv lock --clear

# Install Python dependencies from Pipfile.lock
RUN pipenv install --deploy --ignore-pipfile

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run Django development server
CMD ["pipenv", "run", "python", "django_DS_progect/manage.py", "runserver", "0.0.0.0:8000"]
