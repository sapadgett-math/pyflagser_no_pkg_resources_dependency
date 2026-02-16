from packaging.version import parse

tests = [
    ("1.2.3", "2.0.0"),
    ("1.0rc1", "1.0"),
    ("1.0", "1.0"),
    ("2.0", "1.9.9"),
    ("1.0.post1", "1.0"),
]

for a, b in tests:
    print(a, "<", b, "=>", parse(a) < parse(b))
