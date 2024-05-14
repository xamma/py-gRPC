FROM python:3.12.3-slim

WORKDIR /app

RUN adduser --system --no-create-home nonroot

COPY requirements.txt /opt/requirements.txt

RUN pip install --no-cache-dir -r /opt/requirements.txt

COPY . .

RUN python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. greeter.proto

USER nonroot

EXPOSE 50051

CMD ["python", "server.py"]