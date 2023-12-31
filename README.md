# CodeBERT Features Docker Image

Transforms a code snippet to a list of 768 floats by averaging the
token embeddings from
[CodeBERT](https://huggingface.co/microsoft/codebert-base).

# How to Run

Use [Docker](https://www.docker.com/get-started/) to pull the
pre-built image and run it on your machine:

```sh
docker network create --driver bridge codebert-features
# add ``--gpus all`` flag to use GPU
docker run --name codebert-features -p 7860:7860 --network codebert-features -d inpefess/codebert-features
# run this to collect Prometheus metrics
docker run --name prometheus -p 9090:9090 -v ./prometheus.yml:/etc/prometheus/prometheus.yml --network codebert-features -d prom/prometheus
```

Then access, for example, using standard Python libraries:

```python
import json
from urllib.parse import urlencode
from urllib.request import urlopen

CODE_SNIPPET = """
def main() -> None:
    return

"""
data = {"code_snippet": CODE_SNIPPET}
with urlopen(f"http://127.0.0.1:7860/?{urlencode(data)}") as response:
    embedding = response.read().decode("utf8")
print(json.loads(embedding))
```

# How to Build a New Version

Feel free to modify the source code, build and run a new image:

```sh
git clone https://github.com/inpefess/codebert-features
cd codebert features
docker build -t my-codebert-features .
```
