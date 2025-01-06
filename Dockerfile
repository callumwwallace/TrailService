# Use Docker BuildKit syntax (allows specifying platform in FROM)
# syntax=docker/dockerfile:1.4

FROM --platform=linux/amd64 python:3.9-slim-bullseye

# Environment variables (optional but useful)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# 1. Install dependencies for Microsoft repositories
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# 2. Add Microsoft’s GPG key and repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list \
       > /etc/apt/sources.list.d/mssql-release.list

# 3. Install msodbcsql17 and dependencies
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql17 \
    unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project
COPY . /app/

# (Optional) Expose a port (e.g., 8000)
EXPOSE 8000

# Default command to run your app
CMD ["python", "app.py"]