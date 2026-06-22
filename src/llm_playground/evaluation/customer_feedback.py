import time

import pandas as pd

from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.evaluation.models import (
    EvaluationResult,
)

class CustomerFeedbackEvaluator:

    def __init__(
        self,
        analyst: CustomerFeedbackAnalyst,
    ):
        self.analyst = analyst

def evaluate(
    self,
    dataset_path: str,
    output_path: str | None = None,
) -> EvaluationResult:
    
    df = pd.read_csv(
        dataset_path
    )
    
    results = []

    for idx, row in df.iterrows():

        print(
            f"Processing {idx + 1}/{len(df)}..."
        )

        start = time.time()

        prediction = self.analyst.analyze(
            row["feedback"]
        )

        if output_path:
            df.to_csv(
                output_path,
                index=False,
            )

        latency = (
            time.time()
            - start
        )

        results.append(
            {
                "predicted_topic":
                    prediction.topic.value,

                "predicted_sentiment":
                    prediction.sentiment.value,

                "latency":
                    latency,
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

    average_latency = (
        df["latency"]
    ).mean()

    return EvaluationResult(
        topic_accuracy=topic_accuracy,
        sentiment_accuracy=sentiment_accuracy,
        average_latency=average_latency,
        num_samples=len(df),
    )