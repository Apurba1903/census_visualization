# Base Image
FROM python:3.9

# Working Directory
WORKDIR /app

# Copy
COPY . /app

# Run
RUN pip install -r requirements.txt

# Port
EXPOSE 5000

#Command
CMD ["streamlit","run","./app.py","--server.port=5000"]