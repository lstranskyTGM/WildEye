FROM python:3.12.6

WORKDIR /Bilderkennung

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "AI_Bilderkennung/api_connector.py" ]