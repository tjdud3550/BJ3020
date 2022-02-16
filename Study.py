a= int(input())
b=int(input())
c= int(input())

cnt = 0


answer = []
answer = (a*b*c)


for i in range(10):
    for j in range(len(answer)):
        if answer[i] == i:
            cnt += 1
print(cnt)
#0이 몇번 쓰였는지 출력하는 첫번째 반복문
#1-9까지 몇번쓰였는지 확인 