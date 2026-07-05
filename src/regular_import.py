import time
start = time.perf_counter()

import json

elapsed_normal = time.perf_counter() - start
print(f"通常import:        {elapsed_normal:.6f}秒")

