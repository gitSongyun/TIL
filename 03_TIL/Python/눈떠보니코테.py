import re 

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

q = queries[0].replace('?', '.')

pattern = re.compile(q)

for word in words:
    match_pattern = pattern.findall(word)
    