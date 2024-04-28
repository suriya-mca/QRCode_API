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
COPY ./requirements.txt /app

# Install dependencies
RUN pip install --upgrade pip && \
	pip install --no-cache-dir --upgrade -r requirements.txt

# Expose ports and define startup commands based on selected framework
EXPOSE 8000

# Specify the entry point (Replace "mail" with your actual file name)
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]