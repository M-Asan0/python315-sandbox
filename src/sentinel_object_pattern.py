import copy

_MISSING = object()

def greet(name: object = _MISSING):     # 専用の型を表現できないため、objectなどで受けることになる
    if name is _MISSING:
        print("何も渡されてない")
    else:
        print(f"渡された: {name}")

greet()             # 何も渡されてない
greet(None)         # 渡された: None

print(_MISSING)     # <object object at 0x722c62e90250>

# オブジェクトのコピー
config = {"timeout": _MISSING}

config_copy = copy.deepcopy(config)
print(config_copy["timeout"] is _MISSING)  # False 別物になる

