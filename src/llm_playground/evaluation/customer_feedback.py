from pathlib import Path
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

        failed_predictions = 0

        for idx, row in df.iterrows():

            print(
                f"Processing {idx + 1}/{len(df)}..."
            )

            start = time.time()

            try:
                prediction = self.analyst.analyze(
                    row["feedback"]
                )

            except Exception as e:
                
                failed_predictions += 1

                results.append(
                    {
                        "predicted_topic": None,
                        "predicted_sentiment": None,
                        "latency": None,
                    }
                )

                print(
                    f"Failed on row {idx}: {e}"
                )

                continue

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
        
        successful_predictions = (
            len(df)
            - failed_predictions
        )

        success_rate = (
            successful_predictions
            / len(df)
        )

        predictions = pd.DataFrame(
            results
        )

        df = pd.concat(
            [df, predictions],
            axis=1,
        )

        if output_path:

            Path(output_path).parent.mkdir(
                parents=True,
                exist_ok=True,
            )

            df.to_csv(
                output_path,
                index=False,
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
            model_name=self.analyst.provider.model,
            failed_predictions=failed_predictions,
            successful_predictions=successful_predictions,
            success_rate=success_rate,
        )