# Use Python 3.13.1 image
FROM python:3.13.1-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire project to the container
COPY . /app

# Expose the Streamlit default port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "Dashboard/app.py", "--server.port=8501", "--server.enableCORS=false"]
