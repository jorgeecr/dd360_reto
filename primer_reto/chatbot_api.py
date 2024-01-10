from chatbots import Agent
from dotenv import load_dotenv
from fastapi import Body, FastAPI, File, Form, HTTPException, UploadFile

load_dotenv()  # This loads variables from .env into the environment

app = FastAPI()


# API endpoint for chatbot
@app.post("/chatbot")
async def chatbot_api(
    message: str = Form(...),
    use_openai: bool = Form(True),
    csv_file: str = Form(...),
):
    try:
        chatbot = Agent(use_openai=use_openai, csv_path=csv_file)
        # Process the message using the chatbot
        response = chatbot.ask(message)

        # Return the chatbot's response
        return {"response": response}

    except Exception as e:
        # Handle exceptions or errors
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    # Run the FastAPI app with Uvicorn on port 5000
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
