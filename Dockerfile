FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create output directory
RUN mkdir -p output

# use -u to avoid buffering
# CMD ["python", "-u", "main.py"]