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
    print(f"代入エラー: {e}")           # 代入エラー: 'frozendict' object does not support item assignment

# ── 4. hashable → dict のキーになれる ────────
print()
print("=== hashable ===")
print(f"hash(fd) = {hash(fd)}")        # 7517883790508650510

cache = {fd: "result"}
print(f"dict のキーとして使用: {cache[fd]}")    # result

try:
    hash(d)
except TypeError as e:
    print(f"通常 dict は hash 不可: {e}")       # unhashable type: 'dict'

# dictはhash不可な理由
# https://docs.python.org/3/reference/datamodel.html#object.__hash__
# If a class defines mutable objects and implements an __eq__() method, it should not implement __hash__(), since the implementation of hashable collections requires that a key's hash value is immutable.
# 意訳すると「変更可能なオブジェクトは __hash__ を実装すべきでない。なぜなら hash の値は不変である必要があるから」

try:
    cache = {d: 'result'}
except TypeError as e:
    print(f'TypeError: {e}')                   # cannot use 'dict' as a dict key (unhashable type: 'dict')

# dict のキーになるには hashable である必要があり、通常の dict は hashable じゃないのでエラーになる

# ── 5. set に入れられる ───────────────────────
print()
print("=== set ===")
fd1 = frozendict({"x": 1})
fd2 = frozendict({"x": 1})
fd3 = frozendict({"x": 2})
s = {fd1, fd2, fd3}
print(f"同じ内容は重複なし: {s}")

d1 = {"x": 1}
d2 = {"x": 1}
try:
    s = {d1, d2}
except TypeError as e:
    print(f"TypeError: {e}")            # cannot use 'dict' as a set element (unhashable type: 'dict')
    
# setもhashで重複判定しているためhashableである必要がある
# https://docs.python.org/3/glossary.html#term-hashable
# Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.
# dict と set は内部的に hash 値を使っている

# ── 6. lru_cache と組み合わせ ─────────────────
print()
print("=== lru_cache ===")

@functools.lru_cache
def expensive(mapping):
    return sum(mapping.values())

print(f"1回目: {expensive(fd)}")
print(f"2回目(キャッシュ): {expensive(fd)}")
print(f"キャッシュ情報: {expensive.cache_info()}")
