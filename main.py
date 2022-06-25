qna = {
    "hi":"hey",
    "how are you":"i am fine",
    "what is your name":"my name is aditya",
}

while True:
    qs = input()

    if(qs == "quit"):
        break

    else:
        print(qna[qs])