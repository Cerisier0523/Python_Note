import math
height = float(input("请输入身高：(厘米)"))/100
weight = float(input("请输入体重：(公斤)"))
bmi = weight/math.pow(height,2)
print("BMI 数值为：{:.2f}".format(bmi))
who,dom="",""
if bmi < 18.5:
  who, dom ="偏瘦","偏瘦"
elif bmi < 24:
  who, dom ="正常","正常"
if bmi < 25:
  who, dom ="正常","偏胖"
elif bmi < 30:
  who, dom ="肥胖","肥胖"
elif bmi < 30:
  who, dom ="肥胖","肥胖"

print("BMI 指标为:国际{0}; 国内{1}".format(who,dom))
#{0} 和 {1} 是 Python 字符串格式化的占位符
print(f"BMI 指标为:国际'{who}'; 国内'{dom}'")
#单引号保障输出一致

