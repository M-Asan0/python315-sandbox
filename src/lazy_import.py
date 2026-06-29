lazy import time
start = time.perf_counter()

lazy import json

elapsed_lazy = time.perf_counter() - start
print(f"lazy import宣言時: {elapsed_lazy:.6f}秒")

start = time.perf_counter()
result = json.dumps({"key": "value"})
elapsed_access = time.perf_counter() - start
print(f"lazy 実アクセス時: {elapsed_access:.6f}秒")