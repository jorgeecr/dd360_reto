# SOLUCIONES AL RETO AI 

## Reto obligatorio 


### Descripción general

El directorio `primer_reto` contiene los siguientes documentos:
- chatbots.py
- chatbot_api.py
- chatbot_api_request_example.ipynb
- prompts.py
- llama_csv_demo.ipynb

La solución principal está en el archivo `chatbots.py`. Este archivo contiene la función del reto obligatorio. Existen dos opciones en cuanto a modelos usados: OpenAI ChatGPT y Llama2. En el primer caso hay que usar un API key proporcionado por OpenAI; en el segundo caso hay que cargar el modelo localmente usango Hugging Face Hub (y se recomienda usarlo con un GPU). El notebook `llama_csv_demo.ipynb` es un demo del flujo para este caso y fue hecho en Goggle Colab con una instancia de GPU (version free tier). 



### Uso del API 

Para correr el API, ejecutar los siguientes comandos en la terminal:
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