import re

N = int(input())
list1 = ["VALID" if re.findall("\\b(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE \
|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART \
| GROOVY|OBJECTIVEC)$",input()) else "INVALID" for _ in range(N)]

print(*list1, sep='\n')