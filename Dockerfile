# Use Alpine version of Python 3.12
FROM python:3.12-alpine

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1

# Set working directory
WORKDIR /app

# Copy current directory contents into the container at /app
COPY ./app /app
COPY ./conf/gunicorn.conf.py /etc/gunicorn/gunicorn.conf.py
COPY ./requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip && \
	pip install --no-cache-dir --upgrade -r requirements.txt

# Expose ports and define startup commands based on selected framework
EXPOSE 8000

# Specify the entry point
CMD ["gunicorn", "main:app", "-c", "/etc/gunicorn/gunicorn.conf.py"]