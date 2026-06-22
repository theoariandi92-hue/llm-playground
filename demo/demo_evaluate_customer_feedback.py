import pandas as pd

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

df = pd.read_csv(
    "data/customer_feedback_eval.csv"
)

analyst = CustomerFeedbackAnalyst()

predictions = []

for feedback in df["feedback"]:

    result = analyst.analyze(
        feedback
    )

    predictions.append(
        result.topic
    )

df["predicted_topic"] = predictions

print(df)