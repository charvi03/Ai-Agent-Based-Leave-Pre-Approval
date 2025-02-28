# Use an official Python image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Default command to keep the container running (so we can exec into it)
CMD ["tail", "-f", "/dev/null"]
