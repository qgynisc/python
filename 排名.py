#假定输入都是正确的，不进行错误捕捉，只实现核心功能。
num          = int(input('请输入选手数（1<=N<=100）：'))
score        = input('请输入选手成绩，用空格分开：')
target_score = int(input('请输入要查寻名次的成绩：'))
score_list, rangking = [], 0
for x in score.split():
    score_list.append(int(x))
if num != len(score_list):
    print('***输入成绩数量有误,请重新运行***')
    exit()
for y in score_list:
    if y > target_score:
        rangking += 1
print(rangking+1)