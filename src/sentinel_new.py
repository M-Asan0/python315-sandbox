import copy

MISSING = sentinel('MISSING')

def greet(name: str | None | MISSING = MISSING):    # 文字列、None、未指定マーカーのどれかに限定できる
    if name is MISSING:
        print("何も渡されてない")
    else:
        print(f"渡された: {name}")

greet()             # → 何も渡されてない
greet(None)         # → 渡された: None

print(MISSING)      # → MISSING

# オブジェクトのコピー
config = {"timeout": MISSING}

config_copy = copy.deepcopy(config)
print(config_copy["timeout"] is MISSING)  # True 同一性が保たれる