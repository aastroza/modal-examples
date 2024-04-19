"""
Contains only definitions of Modal objects, to be imported
from other modules.
"""

import modal

image = modal.Image.debian_slim(
    python_version="3.10"
).pip_install(
    "datasets~=2.7.1",
    "dill==0.3.4",  # pinned b/c of https://github.com/uqfoundation/dill/issues/481
    "evaluate~=0.3.0",
    "loguru~=0.6.0",
    "pyarrow~=10.0.1",
    "scikit-learn~=1.1.3",  # Required by evaluate pkg.
    "torch~=1.13.0",
    "transformers~=4.24.0",
)

app = modal.App(name="example-spam-detect-llm", image=image)  # Note: prior to April 2024, "app" was called "stub"
# Used to store datasets, trained models, model metadata, config.
volume = modal.Volume.from_name(
    "example-spam-detect-vol", create_if_missing=True
)
