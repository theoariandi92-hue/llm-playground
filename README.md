# llm-playground

An example repository demonstrating how to train a LLaMA-style language model and set up a Retrieval-Augmented Generation (RAG) serving stack using FastAPI.

This project is intended as a learning / reference implementation and does not include model weights. It shows recommended components and example commands to prepare data, fine-tune (or LoRA-finetune) a LLaMA model, build a vector index (FAISS), and serve RAG queries via a FastAPI application.

---

## Features

- Instructions for preparing LLaMA-compatible model weights (note: weights NOT included)
- Example training workflow (fine-tuning / LoRA) using Hugging Face Transformers / PEFT
- Building a vector index for RAG using sentence-transformers + FAISS
- A minimal FastAPI server that performs retrieval + generation
- Example Docker and docker-compose snippets to run the serving stack

---

## Requirements

- Linux or macOS (Linux recommended for GPUs)
- Python 3.9+ (3.10+ recommended)
- CUDA-enabled GPU with recent drivers for training and inference (optional for CPU-only experiments)
- Disk space for model weights and vector indexes

Python packages (example):

- torch (with CUDA if using GPU)
- transformers
- accelerate
- peft
- datasets
- sentence-transformers
- faiss-cpu or faiss-gpu
- fastapi
- uvicorn
- pydantic
- python-multipart (optional for uploads)

You can install common dependencies with:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

(If this repo doesn't include requirements.txt, create one with packages above pinned to versions that match your environment.)

---

## Important notes about model weights and licenses

LLaMA-style models (Meta LLaMA, etc.) are distributed under their own license and are NOT included in this repository. You must obtain model weights yourself and place them into the expected folder (example: `models/llama/`). Follow the official distribution and license terms for any model you use.

When using third-party or commercial models, ensure you comply with their license and usage restrictions.

---

## Quickstart

1. Clone the repo

```bash
git clone https://github.com/theoariandi92-hue/llm-playground.git
cd llm-playground
```

2. Create virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate
# (optional) install the UV package manager
# - install inside the virtual environment:
pip install uv
# - or install system-wide using pipx:
# pipx install uv

# then install project dependencies (if you prefer requirements file):
pip install -r requirements.txt

# or, if using UV, install dependencies via UV (see pyproject.toml):
# uv install
```

3. Place model weights

- Create `models/llama/` and put your LLaMA-compatible model there. This repository expects the model to be loadable by Hugging Face Transformers or by your chosen inference code.

4. Prepare your knowledge/base documents for RAG

- Put text files or a CSV/JSONL of documents in `data/docs/`.

5. Create embeddings and build FAISS index

A minimal example to create embeddings and index (python):

```python
from sentence_transformers import SentenceTransformer
import faiss
import json

embedder = SentenceTransformer('all-MiniLM-L6-v2')  # or another model

docs = []
with open('data/docs/my_docs.jsonl') as f:
    for line in f:
        docs.append(json.loads(line))

# assume docs is a list of {'id': ..., 'text': ...}
texts = [d['text'] for d in docs]
embs = embedder.encode(texts, convert_to_numpy=True)

index = faiss.IndexFlatL2(embs.shape[1])
index.add(embs)
faiss.write_index(index, 'indexes/faiss.index')

# Save metadata for retrieval
import pickle
with open('indexes/metadata.pkl', 'wb') as f:
    pickle.dump(docs, f)
```

6. Run FastAPI server (example)

Create a file `app/main.py` (example skeleton provided below) and start server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Example FastAPI skeleton for RAG (app/main.py):

```python
from fastapi import FastAPI
from pydantic import BaseModel
import faiss
import pickle
from sentence_transformers import SentenceTransformer

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

# load index and metadata on startup
embedder = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('indexes/faiss.index')
with open('indexes/metadata.pkl', 'rb') as f:
    metadata = pickle.load(f)

@app.post('/query')
async def query(req: QueryRequest):
    q_emb = embedder.encode([req.query])
    D, I = index.search(q_emb, req.top_k)
    retrieved = [metadata[i] for i in I[0]]

    # TODO: call LLM for generation using retrieved context.
    # Example: concatenate retrieved texts into prompt and send to the model.

    return {
        'query': req.query,
        'results': retrieved,
        'generation': 'TODO: integrate model generation here'
    }
```

Note: For generation you can use the loaded LLaMA model (via Transformers) or an external API. If using an on-device LLaMA you may need to use a param-efficient method (quantization/ggml) or a server like text-generation-inference.

---

## Training / Fine-tuning (high-level)

This section outlines common approaches; choose the one that fits your resources.

Option A — Full fine-tuning (heavy)

- Requires large GPU memory across devices and distributed training.
- Typical stack: Hugging Face Transformers + accelerate, prepare dataset with `datasets`, run training script that implements Trainer or custom training loop.

Option B — Adapter / LoRA fine-tuning (recommended for resource-constrained setups)

- Use PEFT/LoRA to fine-tune only low-rank adapters.
- Example pseudo-steps:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import get_peft_model, LoraConfig

model = AutoModelForCausalLM.from_pretrained('path/to/llama')
tokenizer = AutoTokenizer.from_pretrained('path/to/llama', use_fast=False)

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=['q_proj', 'v_proj'],
    lora_dropout=0.05,
    bias='none'
)
model = get_peft_model(model, lora_config)

# prepare Dataset and Trainer, then train
```

- Save the adapter weights (much smaller than full model) and load them at inference time on top of the base weights.

Important: Always test training with a small dataset and enable gradient checkpointing / mixed precision (fp16) to conserve memory.

---

## Docker example (minimal)

Dockerfile (very small example):

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

docker-compose (example to run API + persistent volume for indexes):

```yaml
version: '3.8'
services:
  api:
    build: .
    volumes:
      - ./indexes:/app/indexes
      - ./models:/app/models
    ports:
      - 8000:8000
    environment:
      - ENV=production
```

---

## Usage example (curl)

```bash
curl -X POST "http://localhost:8000/query" -H "Content-Type: application/json" -d '{"query": "What is retrieval augmented generation?", "top_k": 3}'
```

---

## Troubleshooting

- Out of memory errors: enable mixed precision (fp16), gradient checkpointing, or use LoRA.
- FAISS GPU vs CPU: use `faiss-gpu` when performing large-scale indexing with GPUs.
- Tokenizer/model mismatch: ensure you use the tokenizer that matches your model.

---

## Contributing

Contributions are welcome. Create issues for feature requests or bugs, and open PRs for fixes. If you add scripts or notebooks, please include clear README sections explaining how to run them.

---

## Credits and references

- This repository is a learning example and borrows common community practices for fine-tuning and RAG pipelines.

---

## License

Specify a license for this repository (MIT, Apache-2.0, etc.) and ensure any included content (models, datasets) respects their licenses.
