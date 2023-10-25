import os


def open_work_space():
    path = 'E:\zhuyu\workspace'
    os.system("start explorer %s" % path)
    
def open_project():
    path = 'E:\project'
    os.system("start explorer %s" % path)

def open_ssr():
    path = r'E:\software\ssrr\ShadowsocksR-Win64-6.0.4\ShadowsocksR'
    os.system("start explorer %s" % path)

def open_vm():
    path = r'E:\vm'
    os.system("start explorer %s" % path)



if __name__ == '__main__':
    select = input("1:open workspace  2:open project 3:ssr 4:vm \n")
    if "1" == select:
        open_work_space()
    elif "2" == select:
        open_project()
    elif "3" == select:
        open_ssr()
    elif "4" == select:
        open_vm()    
    else:
        pass


