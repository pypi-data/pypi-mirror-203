import platform, os
from .Windows import main as main_windows
from .Linux import main as main_linux
from .Android import main as main_android

def main():
    OS = platform.system()

    if OS == 'Windows':                     wifi = main_windows()
    else:
        if os.path.exists('/data/data'):    wifi = main_android()
        else:                               wifi = main_linux()

    return wifi


if __name__ == '__main__':
    main()