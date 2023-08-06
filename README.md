---
title: CodeBERT Features
sdk: docker
license: apache-2.0
---

Transforms a code snippet to a list of 768 floats by averaging the
token embeddings from
[CodeBERT](https://huggingface.co/microsoft/codebert-base).

See an
[example](https://huggingface.co/spaces/inpefess/codebert-features?code_snippet=print%28%22Hello%2C+world%21%22%29)
running on Hugging Face.

# Run Locally

Use [Docker](https://www.docker.com/get-started/) to pull the
pre-built image and run it on your machine:

```sh
docker run -it -p 7860:7860 inpefess/codebert-features
```

Then access, for example, using the
[requests](https://requests.readthedocs.io) library:

```python
import json
import requests

code_snippet = """
def square(x: int) -> int:
    return x ** 2

"""

response = requests.get(f"http://localhost:7860?code_snippet={code_snippet}")
embeddings = json.loads(response.content)["output"]
```

# Build Locally

Feel free to modify the source code, build and run a new image:

```sh
git clone https://github.com/inpefess/codebert-features
cd codebert features
docker build -t my-codebert-features .
docker run -it -p 7860:7860 my-codebert-features
```
