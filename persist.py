from typing import Dict

import modal

from modal import Stub, web_endpoint

stub = Stub()
CACHE_DIR = "/cache"
pendrive = modal.SharedVolume().persist()

@stub.function(
    shared_volumes={CACHE_DIR: pendrive}
    print(hello)
)

@web_endpoint(method="POST")
def square(item: Dict):
    return {"square": item['x']**2}