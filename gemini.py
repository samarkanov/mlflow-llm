import mlflow
import google.genai as genai
import os

JUDGE_MODEL="gemini-2.5-flash"



# Optional: Set a tracking URI and an experiment
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("Gemini")

with mlflow.start_run() as evaluation_run:
    mlflow.log_param("judge_model_name", JUDGE_MODEL)

    # Configure the SDK with your API key.
    client = genai.Client(api_key=os.environ["GOOGLE_GEMINI_API_KEY"])

    # Use the generate_content method to generate responses to your prompts.
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="select the best reply: " + 
    )

    mlflow.log_param("response", response.text)