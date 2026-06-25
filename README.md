# LLM Playground

A personal project for learning how to build, evaluate, and deploy LLM-powered applications.

Most LLM tutorials focus on prompting a model. This project focuses on everything around the model: structured outputs, evaluation pipelines, benchmarking, testing, provider abstraction, and API serving.

The goal is to better understand practical questions such as:

* Which model performs best for a given task?
* How much latency am I paying for higher accuracy?
* How reliable are structured outputs across different models?
* How can LLM applications be tested and evaluated systematically?

---

# Features

* Customer feedback analysis

  * Topic classification
  * Sentiment classification
  * Feedback summarization
* Structured outputs using Pydantic
* Local inference using Ollama
* OpenAI provider support
* Provider abstraction layer
* Automated evaluation framework
* Multi-model benchmarking
* Unit testing with MockProvider
* REST API using FastAPI

---

# Architecture

```text
Client
  ↓
FastAPI
  ↓
CustomerFeedbackAnalyst
  ↓
BaseLLMProvider
     ├── OllamaProvider
     ├── OpenAIProvider
     └── MockProvider
  ↓
LLM
```

The project separates application logic from model providers, making it easier to switch between Ollama, OpenAI, or future providers without changing downstream code.

---

# Project Structure

```text
src/
└── llm_playground/
    ├── api/
    │   ├── app.py
    │   └── models.py
    │
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
        └── providers/
            ├── base.py
            ├── ollama.py
            ├── openai.py
            └── mock.py

tests/
├── test_topics.py
├── test_sentiments.py
└── test_analyzer.py

demo/
data/
output/
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

Start Ollama:

```bash
ollama serve
```

Verify:

```bash
ollama list
```

---

# OpenAI Setup

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
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

Example output:

```text
Topic.DELIVERY

Sentiment.NEGATIVE

Customer experienced delayed delivery and did not receive support response.
```

---

# Evaluation Framework

Run evaluation against a labeled dataset:

```bash
uv run python demo/demo_ollama_customer_feedback_evaluate.py
```

Metrics tracked:

* Topic Accuracy
* Sentiment Accuracy
* Average Latency
* Failed Predictions

Evaluation outputs are saved to:

```text
output/
```

---

# Model Benchmarking

Compare multiple models:

```bash
uv run python demo/demo_ollama_customer_feedback_compare_models.py
```

Example benchmark results:

| Model       | Topic Accuracy | Sentiment Accuracy | Avg Latency (s) |
| ----------- | -------------- | ------------------ | --------------- |
| qwen3:8b    | 80%            | 100%               | 50.5            |
| qwen2.5:7b  | 90%            | 90%                | 5.8             |
| llama3.2:3b | 60%            | 70%                | 2.3             |

The purpose of benchmarking is not to find the "best" model, but to understand the trade-offs between accuracy, latency, cost, and output reliability.

---

# Unit Testing

Run all tests:

```bash
uv run pytest
```

Current test coverage includes:

* Topic enum validation
* Sentiment enum validation
* CustomerFeedbackAnalyst parsing
* MockProvider integration

The project uses MockProvider to keep tests deterministic and independent of external LLMs.

---

# FastAPI API

Start the API server:

```bash
uv run uvicorn llm_playground.api.app:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Analyze Feedback Endpoint

## Request

```http
POST /analyze-feedback
```

```json
{
  "feedback": "My package arrived 5 days late and support never replied."
}
```

## Response

```json
{
  "topic": "Delivery",
  "sentiment": "Negative",
  "summary": "Customer experienced delayed delivery and did not receive support response."
}
```

---

# Development Workflow

```text
Prompt Development
        ↓
Unit Tests
        ↓
Evaluation Dataset
        ↓
Benchmark Multiple Models
        ↓
Deploy Through FastAPI
```

---

# Design Principles

A few principles I try to follow throughout the project:

* Keep business logic independent from model providers
* Use structured outputs instead of parsing free-form text
* Evaluate models using labeled datasets rather than subjective judgement
* Make components testable using mocks and dependency injection
* Prefer simple, reusable building blocks over framework-heavy solutions

---

# Tech Stack

* Python
* Ollama
* OpenAI API
* FastAPI
* Pydantic
* Pandas
* Pytest
* uv

---

# Next Steps

* Add Gemini and Anthropic providers
* Expand evaluation datasets
* Add benchmark reporting
* Experiment with RAG pipelines
* Build simple agent workflows
* Containerize the application with Docker

---

# Why This Project?

Most LLM demos stop at generating a response.

This project focuses on the surrounding engineering challenges:

* Structured outputs
* Evaluation and benchmarking
* Provider abstraction
* Testing
* API development
* Building reusable application components

The goal is to better understand how to select, evaluate, and deploy language models using measurable engineering metrics rather than relying solely on subjective comparisons.
