# encoding=utf-8
import re

string = "Hello world! To be Releax"
pattern = "[abc]"

result = re.finditer(pattern, string)
for item in result:
    print(item.start(), item.end())
    print(string[item.start():item.end()])
