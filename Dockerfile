FROM python:3.13
# Set working directory
WORKDIR /app

COPY pyproject.toml /app/
RUN pip install -e .  # This will install the dependencies from pyproject.toml
   
# Copy the FastAPI app into the container
COPY . /app/

# Expose port 8000 (default for FastAPI)
EXPOSE 8000

# Command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]