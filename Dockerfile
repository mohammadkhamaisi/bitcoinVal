FROM python

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY avgval.py .
EXPOSE 5000
CMD ["python","/app/avgval.py"]
