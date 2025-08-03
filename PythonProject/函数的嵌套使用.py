def happy():
    print('Happy Birthday')
def happyB(name):#函数中对happy()的调用
    happy()
    happy()
    print('Happy Birthday,dear{}'.format(name))
    happy()

happyB('Mike')#主函数中对happyB的调用