# LLM Playground

A hands-on project for learning how to build AI applications using local LLMs.

The current implementation uses Ollama and Qwen 3 to analyze customer feedback and extract:

- Topic
- Sentiment
- Summary

The goal of this project is to learn the complete AI application stack:

- Local LLM inference
- Prompt engineering
- Python packaging
- Provider abstraction
- API serving
- Structured outputs

---

## Example

### Input

```text
The delivery arrived 5 days later than promised and customer support never replied to my emails. The product itself works well.
```

### Output

```json
{
  "topic": "Delivery Delay",
  "sentiment": "Negative",
  "summary": "Customer experienced a significant delivery delay and did not receive a response from customer support."
}
```

---

## Architecture

```text
CustomerFeedbackAnalyst
        ↓
    OllamaProvider
        ↓
       Ollama
        ↓
      Qwen3 8B
```

### Responsibilities

| Component | Responsibility |
|------------|---------------|
| CustomerFeedbackAnalyst | Business logic and prompt construction |
| OllamaProvider | Communication with Ollama |
| Ollama | Model runtime |
| Qwen3 8B | Language model |

---

## Project Structure

```text
src/
└── llm_playground/
    ├── llm/
    │   ├── base.py
    │   └── providers/
    │       ├── ollama.py
    │       └── openai.py
    │
    └── customer_feedback/
        ├── prompts.py
        ├── analyzer.py
        └── models.py

demo/
├── demo_ollama.py
├── demo_provider.py
└── demo_customer_feedback.py
```

---

## Prerequisites

### Install Ollama

```bash
brew install ollama
```

Start the Ollama server:

```bash
ollama serve
```

Download the model:

```bash
ollama pull qwen3:8b
```

Verify:

```bash
ollama list
```

---

## Installation

```bash
git clone <repo-url>
cd llm-playground
uv sync
```

---

## Running the Demo

```bash
uv run python demo/demo_customer_feedback.py
```

---

## Usage

```python
from llm_playground.customer_feedback.analyzer import (
    CustomerFeedbackAnalyst,
)

analyst = CustomerFeedbackAnalyst()

result = analyst.analyze(
    '''
    Delivery was delayed by 4 days.
    Customer support never replied.
    Product quality was good.
    '''
)

print(result)
```

---

## Design Decisions

### Why separate providers from business logic?

The project separates:

```text
customer_feedback/
```

from:

```text
llm/providers/
```

so that business logic remains independent from the underlying LLM implementation.

Today:

```text
CustomerFeedbackAnalyst
        ↓
    OllamaProvider
        ↓
      Qwen3
```

Tomorrow:

```text
CustomerFeedbackAnalyst
        ↓
    OpenAIProvider
        ↓
       GPT
```

The analyst implementation should not change when switching models.

---

## Current Features

- Local LLM inference using Ollama
- Qwen3 8B support
- Customer feedback analysis
- Topic extraction
- Sentiment classification
- Feedback summarization

---

## Roadmap

### Phase 1
- [ ] Local inference with Ollama
- [ ] Provider abstraction
- [ ] Customer feedback analysis

### Phase 2
- [ ] Structured Pydantic responses
- [ ] OpenAI provider
- [ ] Evaluation framework

### Phase 3
- [ ] FastAPI service
- [ ] REST API endpoint
- [ ] Docker support

### Phase 4
- [ ] RAG
- [ ] Fine-tuning experiments
- [ ] Model benchmarking
