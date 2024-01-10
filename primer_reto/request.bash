curl -X POST -H "Content-Type: multipart/form-data" \
     -F "message=¿Cuál es el precio promedio de los departamentos en venta?" \
     -F "use_openai=true" \
     -F "csv_file=listings.csv" \
     http://localhost:8000/chatbot 