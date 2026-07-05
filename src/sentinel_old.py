import copy

_MISSING = object()

def greet(name: object = _MISSING):     # 型注釈としてはobjectとするしかなく、ただしobjectはあらゆる型を含んでしまう
    if name is _MISSING:
        print("何も渡されてない")
    else:
        print(f"渡された: {name}")

greet()             # → 何も渡されてない
greet(None)         # → 渡された: None

# 困る場面 printしたとき
print(_MISSING)     # print(_MISSING)

# オブジェクトのコピー
config = {"timeout": _MISSING}

config_copy = copy.deepcopy(config)
print(config_copy["timeout"] is _MISSING)  # False 別物になる

