from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

from llm_playground.evaluation.customer_feedback import (
    CustomerFeedbackEvaluator,
)

analyst = CustomerFeedbackAnalyst()

evaluator = CustomerFeedbackEvaluator(
    analyst
)

result = evaluator.evaluate(
    "data/customer_feedback_eval.csv",
)

print(
    f"Topic Accuracy: "
    f"{result.topic_accuracy:.2%}"
)

print(
    f"Sentiment Accuracy: "
    f"{result.sentiment_accuracy:.2%}"
)

print(
    f"Average Latency: "
    f"{result.average_latency:.2f}s"
)