from __init__ import *

def _f_kill(func: callable):
    def _in():
        print(f"Killing {MYTHWARE_MAIN} ...")
        func()
        print(f"Killed {MYTHWARE_MAIN} SUCCESS")

    return _in

def _f_judge(func: callable):
    def _in():
        print(f"Judging {MYTHWARE_MAIN} ...")
        func()
        print(f"Judged {MYTHWARE_MAIN} SUCCESS")

    return _in

@_f_kill
def kill():
    os.system(f"taskkill /f /im {MYTHWARE_MAIN}")

@_f_judge
def judge():
    for i in range(0, 100000):
        pc = psutil.Process(i)
        if pc.name == "StudentMain.exe":
            return True
        
    else:
        return False

