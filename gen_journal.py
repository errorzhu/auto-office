import datetime


def create_journal_file(file_name):
    context = gen_template_context()
    with open(file_name,'a',encoding="utf8") as ff:
        ff.write(context)
        ff.write("\r")


def gen_template_context():
    context = '''
[principal]
    多想想工作的意义
    做重要的事
    假设检验反馈工作法
[task]
[todo]
[problem]
     
    '''
    return  context
if __name__ == '__main__':
    today = datetime.datetime.now().strftime("%Y%m%d")
    file_name=today+".txt"
    create_journal_file(file_name)


