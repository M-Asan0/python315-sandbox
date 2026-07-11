its = [[1, 2, 3], [4, 5], [6]]

# 3.14 ネスト内包表記
combined = [x for sublist in its for x in sublist]
print(combined)

# 3.15 PEP 798 – Unpacking in Comprehensions
combined = [*sublist for sublist in its]
print(combined)