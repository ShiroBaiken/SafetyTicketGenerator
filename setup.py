import PyInstaller.__main__

PyInstaller.__main__.run(['_start.py',
                          '--onefile',
                          '--specpath start.spec'])
