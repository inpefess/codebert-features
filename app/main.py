#   Copyright 2023 Boris Shminke
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""FastAPI application serving CodeBERT featues."""
from typing import List

import torch
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from transformers import pipeline

codebert_pipeline = pipeline(
    task="feature-extraction",
    model="microsoft/codebert-base",
    device="cuda" if torch.cuda.is_available() else "cpu",
)
app = FastAPI()
Instrumentator().instrument(app).expose(app)


@app.get("/")
async def codebert_features(code_snippet: str) -> List[float]:
    """
    Return CodeBERT features of an input code snippet.

    :param code_snippet: an input code snippet
    :returns: a dict with one key (output) mapping to an embedding
    """
    return torch.Tensor(codebert_pipeline(code_snippet)[0]).mean(0).tolist()
