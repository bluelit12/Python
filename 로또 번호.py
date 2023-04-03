import random

def rotto():
    a = []
    while len(a) < 6:
        num = random.randint(1, 45)
        if num not in a:
            a.append(num)
    return sorted(a)

num_2 = int(input('몇번 뽑으실건가요?'))
i = 0
for i in range(num_2):
    print(f"로또게임 {i + 1} : {rotto()}")
