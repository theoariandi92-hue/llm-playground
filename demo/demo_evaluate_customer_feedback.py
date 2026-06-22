import time

import pandas as pd

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

df = pd.read_csv(
    "data/customer_feedback_eval.csv"
)

analyst = CustomerFeedbackAnalyst()

results = []

for idx, row in df.iterrows():

    print(
        f"Processing {idx + 1}/{len(df)}..."
    )

    start = time.time()

    prediction = analyst.analyze(
        row["feedback"]
    )

    latency = time.time() - start

    results.append(
        {
            "predicted_topic": prediction.topic.value,
            "predicted_sentiment": prediction.sentiment.value,
            "latency": latency,
        }
    )

predictions = pd.DataFrame(
    results
)

df = pd.concat(
    [df, predictions],
    axis=1,
)

topic_accuracy = (
    df["expected_topic"]
    ==
    df["predicted_topic"]
).mean()

sentiment_accuracy = (
    df["expected_sentiment"]
    ==
    df["predicted_sentiment"]
).mean()

average_latency = df["latency"].mean()

print("\nResults")
print("=" * 50)

print(
    f"Topic Accuracy: {topic_accuracy:.2%}"
)

print(
    f"Sentiment Accuracy: {sentiment_accuracy:.2%}"
)

print(
    f"Average Latency: {average_latency:.2f}s"
)

print("\nPredictions")
print("=" * 50)

print(df)