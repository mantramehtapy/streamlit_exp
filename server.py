import modal

volume = modal.SharedVolume().persist("gajraj")

stub = modal.Stub()

CACHE_DIR = "/cache"

@stub.function(
    shared_volumes={CACHE_DIR: volume},
    # Set the transformers cache directory to the volume we created above.
    # For details, see https://huggingface.co/transformers/v4.0.1/installation.html#caching-models
    secret=modal.Secret.from_dict({"TRANSFORMERS_CACHE": CACHE_DIR})
)
def run_inference():
    ...