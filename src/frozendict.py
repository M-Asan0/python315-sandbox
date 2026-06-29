import functools

# ── 1. 基本的な作成 ──────────────────────────
d  = {"a": 1, "b": 2}
fd = frozendict({"a": 1, "b": 2})

print("=== 型 ===")
print(f"dict     : {type(d)}")                         # <class 'dict'> 
print(f"frozendict: {type(fd)}")                       # <class 'frozendict'>
print(f"dict のサブクラス?: {isinstance(fd, dict)}")    # false サブクラスではない

# dictのサブクラスではない理由として、
# メソッドを潰しても dict.__setitem__ を直接呼ぶ抜け穴が残るという安全性の問題があるとの説明がある
# ソース https://peps.python.org/pep-0814/

# ── 2. 読み取りは dict と同じ ────────────────
print()
print("=== 読み取り ===")
print(f"fd['a'] = {fd['a']}")           # 1
print(f"keys   = {list(fd.keys())}")    # ['a', 'b']

# ── 3. 変更しようとするとエラー ──────────────
print()
print("=== イミュータブル ===")
try:
    fd["c"] = 3
except TypeError as e:
    print(f"代入エラー: {e}")

# ── 4. hashable → dict のキーになれる ────────
print()
print("=== hashable ===")
print(f"hash(fd) = {hash(fd)}")

cache = {fd: "result"}
print(f"dict のキーとして使用: {cache[fd]}")

try:
    hash(d)
except TypeError as e:
    print(f"通常 dict は hash 不可: {e}")

# ── 5. set に入れられる ───────────────────────
print()
print("=== set ===")
fd1 = frozendict({"x": 1})
fd2 = frozendict({"x": 1})
fd3 = frozendict({"x": 2})
s = {fd1, fd2, fd3}
print(f"同じ内容は重複なし: {s}")

# ── 6. lru_cache と組み合わせ ─────────────────
print()
print("=== lru_cache ===")

@functools.lru_cache
def expensive(mapping):
    return sum(mapping.values())

print(f"1回目: {expensive(fd)}")
print(f"2回目(キャッシュ): {expensive(fd)}")
print(f"キャッシュ情報: {expensive.cache_info()}")
