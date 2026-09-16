# Start with a lightweight Linux environment that already has Python 3.12.
FROM python:3.12-slim
# Inside the container, /app becomes our project directory.
WORKDIR /app
# Copy our dependency list into the container.
COPY requirements-docker.txt .
#Install the Python packages inside the container.
RUN pip install --no-cache-dir -r requirements-docker.txt
# Copy our project into /app.
COPY . .
# Documents that our application uses port 5000
EXPOSE 5000
# This is the command Docker will execute when the container starts.
CMD ["python", "-m", "src.api.app"]