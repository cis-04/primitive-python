print("첫 글자를 보고 단어를 맞추세요.")
print("""
        a
        b
        c
        d
        e       """)
print("힌트 : 동물")
print()

Alphabetgame = {
        "a" : "ant",
        "b" : "bear",
        "c" : "cat",
        "d" : "dear",
        "e" : "eagle"
}
sentence = input("a,b,c,d,e 를 각각 입력해 맞는 답을 확인하세요--------:")
 
if sentence in Alphabetgame:
    print(Alphabetgame[sentence])
else:
    print("알맞은 명령어를 입력하세요")
