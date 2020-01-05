#假定输入都是正确的，不进行错误捕捉，只实现核心功能。
input('请输入选手数（1<=N<=100）：')
cj = input('请输入选手成绩，用空格分开：')
mc_cj = int(input('请输入要查寻名次的成绩：'))
cj_list = []
place = 0
for x in cj.split():
    cj_list.append(int(x))
for y in cj_list:
    if y > mc_cj:
        place += 1
print(place+1)