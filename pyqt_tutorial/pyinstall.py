import os

if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['app.py', '--hidden-import=PyQt5.sip', '-F', '--icon=icon.ico', '--noupx', '--clean', '--paths=C:\ProgramData\Anaconda3\Lib\site-packages\PyQt5']
    run(opts)