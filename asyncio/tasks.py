import os, sys
from subprocess import check_call

class Tasks:
    def __init__(self):
        pass

    def set_env(self, args):
        os.environ["$wifi_ssid"]
        os.environ["$wifi_password"]
        check_call("""echo "wifi_ssid='$wifi_ssid'\nwifi_password='$wifi_password'" | ampy put /dev/stdin env.py""", shell=True)


    def deploy(self, args):
        check_call("ampy run -n install.py", shell=True)

def main():
    tasks = Tasks()

    task_name = sys.argv[1]

    task_func = getattr(tasks, task_name)

    task_func(sys.argv[2:])

main()
