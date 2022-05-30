import platform
import subprocess



def pings(site):
    if platform.system().lower() == 'windows':
        ping = subprocess.Popen(['ping', site], stdout=subprocess.PIPE)
        for i in ping.stdout:
            print(i.decode(encoding='cp866'), end='')
    else:
        ping = subprocess.Popen(['ping', site, '-c', '4'], stdout=subprocess.PIPE)
        for i in ping.stdout:
            print(i.decode(encoding='utf-8'), end='')


pings('yandex.ru')
pings('youtube.com')
