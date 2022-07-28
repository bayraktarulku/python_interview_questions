# Magic 8 Ball siyah-beyaz 8-top'a benzeyen içi boş plastik bir küredir.
# pencere olan yüzü ile cevabı evet/hayır olan sorulara cevap verir.
# Bu uygulama da sorulan sorulara random evet/hayır temalı cevaplar verir.
# cevaplar genişletilebilir, bir hafıza yapısı oluşturularak önceki cevap
# ve sorulara göre farklı cevaplar türetilebilir.
# https://github.com/bayraktarulku/funny-words reposu ile daha keyifli bir app haline getirilebilir.

import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes – definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes Signs point to yes",
    "Reply hazy",
    "try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Dont count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]

print("Hello World")
print(
    "I'm a Magic 8 Ball simulation. I answer your questions. Of course with my own technique^^."
)


def magic_eight_ball():
    print("Ask me a question.")
    input()
    print(answers[random.randint(0, len(answers) - 1)])
    print("Good luck")
    replay()


def replay():
    print("Do you have another question? [Y/N] ")
    reply = input()
    if reply == "Y":
        magic_eight_ball()
    elif reply == "N":
        exit()
    else:
        print("What nonsense questions are these? How old are you?")
        replay()


magic_eight_ball()
