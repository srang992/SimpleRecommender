FROM python:3.7.12-slim-bullseye

WORKDIR movie_recommendation/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]

