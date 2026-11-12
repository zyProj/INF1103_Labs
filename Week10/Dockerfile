FROM python:3.11-slim
WORKDIR /app
COPY inventory_class.py .
COPY product_class.py .
COPY physical_product_class.py .
COPY digital_product_class.py .
COPY can_be_shipped_interface.py .
COPY order_class.py .
COPY orderline_class.py .
COPY supplier_class.py .
CMD ["python", "inventory_class.py"]