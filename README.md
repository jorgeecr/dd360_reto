# SOLUCIONES AL RETO AI DE DD360

## Reto obligatorio 

Para ejecutar la solución al reto obligatorio, ejecutar los siguientes comandos en la terminal:
```
pip install -r requeriments.txt
cd primer_reto
uvicorn chatbot_api:app --reload
```

Para hacer un request al API tenemos dos opciones:
### Usando `curl``

Ejecutar el siguiente comando:

```
curl -X POST -H "Content-Type: multipart/form-data" \
     -F "message=¿Cuál es el precio promedio de los departamentos en venta?" \
     -F "use_openai=true" \
     -F "csv_file=listings.csv" \
     http://localhost:8000/chatbot 
```

### Usando `requests` en Python

Ver el ejemplo incluido en el Jupyter notebook `chatbot_api_request_example.ipynb`. 


## Reto opcional

Incluido en el directorio `segundo_reto`, en el Jupyter notebook `dd360_explained_solution.ipynb`.