text = 'qqq www eee rrr ttt yyy uuu iii \
ooo ppp aaa sss ddd fff ggg hhh jjj kkk \
lll zzz xxx ccc vvv bbb nnn mmm'
m = text.split()
print(m)
for i, x in enumerate(m):
    print('   ' * i + x)
