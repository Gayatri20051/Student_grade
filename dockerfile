# Use official Python image
FROM python:3.13.2-slim

# Set working directory
WORKDIR /app

# Copy application file
COPY . .

RUN pip install pytest

# Run the program
CMD ["python", "stud_grade.py"]
