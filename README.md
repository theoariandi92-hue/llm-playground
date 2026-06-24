# LLM Playground

A hands-on playground for learning LLM application development, evaluation, and model comparison using local and cloud-based language models.

The project focuses on building reusable LLM components, structured outputs, automated evaluation pipelines, and benchmarking frameworks to compare model performance across accuracy, latency, and reliability dimensions.

---

# Features

* Customer feedback analysis

  * Topic classification
  * Sentiment classification
  * Feedback summarization
* Local inference using Ollama
* OpenAI provider support
* Structured outputs using Pydantic
* Automated evaluation framework
* Model benchmarking across multiple LLMs
* Output schema validation
* Reusable provider architecture

---

# Project Structure

```text
src/
└── llm_playground/
    ├── customer_feedback/
    │   ├── analyzer.py
    │   ├── models.py
    │   └── prompts.py
    │
    ├── evaluation/
    │   ├── customer_feedback.py
    │   └── models.py
    │
    └── llm/
        ├── providers/
        │   ├── ollama.py
        │   └── openai.py
        └── base.py

demo/
├── demo_ollama_customer_feedback.py
├── demo_openai_customer_feedback.py
├── demo_ollama_customer_feedback_evaluate.py
└── demo_ollama_customer_feedback_compare_models.py

data/
└── customer_feedback_eval.csv

output/
└── *.csv
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/theoariandi92-hue/llm-playground.git

cd llm-playground
```

## Install Dependencies

```bash
uv sync
```

---

# Ollama Setup

Install Ollama:

https://ollama.com

Pull the models:

```bash
ollama pull qwen3:8b

ollama pull qwen2.5:7b

ollama pull llama3.2:3b
```

Verify:

```bash
ollama list
```

Start Ollama:

```bash
ollama serve
```

---

# OpenAI Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
```

Example:

```python
from dotenv import load_dotenv

load_dotenv()
```

---

# Customer Feedback Analysis

Analyze a single customer feedback:

```python
from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

feedback = """
My package arrived 5 days late and
customer support never replied.
"""

analyst = CustomerFeedbackAnalyst()

result = analyst.analyze(
    feedback=feedback
)

print(result.topic)
print(result.sentiment)
print(result.summary)
```

Example Output:

```text
Topic.DELIVERY

Sentiment.NEGATIVE

Customer experienced a delayed delivery and
received no response from customer support.
```

---

# Evaluation Framework

Run evaluation against a labeled dataset:

```bash
uv run python demo/demo_ollama_customer_feedback_evaluate.py
```

Metrics:

* Topic Accuracy
* Sentiment Accuracy
* Average Latency
* Failed Predictions

Generated outputs:

```text
output/
└── predictions.csv
```

---

# Model Benchmarking

Compare multiple models:

```bash
uv run python demo/demo_ollama_customer_feedback_compare_models.py
```

Example Benchmark Results:

| Model       | Topic Accuracy | Sentiment Accuracy | Avg Latency (s) | Failed Predictions |
| ----------- | -------------- | ------------------ | --------------- | ------------------ |
| qwen3:8b    | 80%            | 100%               | 50.5            | 0                  |
| qwen2.5:7b  | 90%            | 90%                | 5.8             | 0                  |
| llama3.2:3b | 60%            | 70%                | 2.3             | 3                  |

---

# Key Findings

### qwen3:8b

Pros:

* Reliable structured outputs
* Strong sentiment classification

Cons:

* High latency

### qwen2.5:7b

Pros:

* Best balance between accuracy and latency
* Reliable schema adherence
* Suitable for extraction and classification tasks

Cons:

* Slightly lower sentiment accuracy than qwen3

### llama3.2:3b

Pros:

* Fastest inference

Cons:

* Occasionally fails output schema validation
* Less reliable for structured extraction workflows

---

# Design Principles

This project emphasizes:

* Provider abstraction
* Structured outputs
* Reusable evaluation workflows
* Model benchmarking
* Reliability measurement
* Production-oriented LLM development

Rather than focusing solely on prompt engineering, the goal is to evaluate LLM systems end-to-end and make data-driven model selection decisions.

---

# Tech Stack

* Python
* Ollama
* OpenAI API
* Pydantic
* Pandas
* uv

---

# Future Roadmap

## Platform

* Provider interface (`BaseLLMProvider`)
* Model factory pattern
* Prompt versioning

## Evaluation

* Confusion matrix reporting
* Automated benchmark reports
* LLM-as-a-Judge evaluation
* Cost tracking
* Robust error analysis

## Applications

* FastAPI service
* Batch inference pipelines
* Embedding models
* Retrieval-Augmented Generation (RAG)
* Agent workflows

## Engineering

* Unit tests
* Integration tests
* CI/CD pipeline
* Docker support

---

# Learning Objectives

This repository serves as a practical playground for:

* LLM application development
* Prompt engineering
* Structured generation
* Model evaluation
* Benchmarking methodologies
* Production AI system design

The goal is to build intuition around selecting, evaluating, and deploying language models based on measurable business and engineering outcomes rather than model capability alone.
