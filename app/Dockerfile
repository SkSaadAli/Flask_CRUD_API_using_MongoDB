# Use the official Python image as the base image
FROM python:3.8-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Copy the requirements file into the container at /app
# COPY requirements.txt .

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of the application code into the container at /app
# COPY . .

# # Expose the port that the Flask app will listen on
# EXPOSE 5000

# # Define the command to run your Flask app
# CMD ["python", "app.py"]

FROM python:3.8-slim
 
# Create app directory
WORKDIR /app
 
# Install app dependencies
COPY requirements.txt ./
 
RUN pip install -r requirements.txt
 
# Bundle app source
COPY . .
 
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]
