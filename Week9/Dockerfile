FROM python:3.11-slim
WORKDIR /app
COPY inventory_system.py .
COPY inventory_class.py .
COPY product_class.py .
COPY physical_product_class.py .
COPY digital_product_class.py .
COPY can_be_shipped_interface.py .
COPY inventory.json .
CMD ["python", "inventory_system.py"]