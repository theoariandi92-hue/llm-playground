from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.evaluation.customer_feedback import (
    CustomerFeedbackEvaluator,
)

from llm_playground.llm.providers.ollama import (
    OllamaProvider,
)

import pandas as pd

models = [
    "qwen3:8b",
    "qwen2.5:7b",
    "llama3.2:3b",
]

for model in models:

    analyst = CustomerFeedbackAnalyst(
        provider=OllamaProvider(
            model=model,
        )
    )           

    evaluator = CustomerFeedbackEvaluator(
        analyst
    )

    result = evaluator.evaluate(
        dataset_path="data/customer_feedback_eval.csv",
        output_path=f"output/{model}.csv",
    )

    benchmark_results = []

    for model in models:

        analyst = CustomerFeedbackAnalyst(
            provider=OllamaProvider(
                model=model,
            )
        )

        evaluator = CustomerFeedbackEvaluator(
            analyst
        )

        result = evaluator.evaluate(
            dataset_path="data/customer_feedback_eval.csv",
            output_path=f"output/{model}.csv",
        )

        benchmark_results.append(
            {
                "model": result.model_name,
                "topic_accuracy": result.topic_accuracy,
                "sentiment_accuracy": result.sentiment_accuracy,
                "avg_latency": result.average_latency,
                "num_samples": result.num_samples,
                "failed_predictions": result.failed_predictions,
            }
        )

    benchmark_df = pd.DataFrame(
        benchmark_results
    )

    print("\nModel Comparison")
    print("=" * 80)

    print(
        benchmark_df.to_string(
            index=False,
            float_format=lambda x: f"{x:.2f}",
        )
    )