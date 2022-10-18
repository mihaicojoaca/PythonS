import os
import sys
import subprocess

clear = lambda: os.system('cls')

def install(package: str):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

def is_installed(package: str):
    try:
        __import__(package)
        return True
    
    except ImportError:
        return False
    
    except Exception as e:
        print(f'Unexpected error: {e} while checking if {package} is installed')
        return True

def get_pending_packages():
    pending = []
    with open('requirements.txt', 'rt') as f:
        requirements = f.read().splitlines()
        for package in requirements:
            if package and not is_installed(package):
                pending.append(package)
    return pending

def setup():
    pending = get_pending_packages()

    if not pending:
        return print('Inst.')

    print(f'{len(pending)} o iei la mue.\n\tTi-ar place sa o iei la muie pe dorina? (da/nu)')

    if input().lower() == 'da':
        for package in pending:
            print(f'Installing {package}...')
            install(package)
        print('Dorina a fost luata la pula.')
    elif input().lower() == 'nu':
        for package in pending:
            print(f'Installing {package}...')
            install(package)
        print('Dorina a fost luata la pula.')
    else:
        print('Installation cancelled')   

def main():
    try:
        clear()
        setup()

    except KeyboardInterrupt:
        print('Installation cancelled')

if __name__ == '__main__':
    main()
else:
    print("Installer is not allowed to be ran.!")
