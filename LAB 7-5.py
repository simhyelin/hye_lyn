import random
random_list = []
for _ in range(3):
    num = random.randrange(0, 101, 5)
    random_list.append(num)

print("0에서 100 이하의 정수 중에서 5의 배수")
print(random_list)
import random
result = random.sample(range(1, 11), 3)
print("1에서 10 사이의 임의의 정수 :", result)
