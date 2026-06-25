from fastapi import FastAPI

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.api.models import (
    AnalyzeFeedbackRequest,
)

app = FastAPI()

analyst = CustomerFeedbackAnalyst()


@app.get("/")
def root():

    return {
        "message": "LLM Playground API"
    }


@app.post(
    "/analyze-feedback"
)
def analyze_feedback(
    request: AnalyzeFeedbackRequest,
):

    result = analyst.analyze(
        feedback=request.feedback
    )

    return result