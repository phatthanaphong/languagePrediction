# 
FROM python:3.9

# 
WORKDIR /language

# 
COPY ./requirements.txt /language/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /language/requirements.txt

# 
COPY ./app /language/app
COPY ./model /language/model

ENV PYTHONPATH "${PYTHONPATH}:/language"

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]