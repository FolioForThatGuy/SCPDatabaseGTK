import sys
from cx_Freeze import setup, Executable

options = dict(


build_exe=dict({'path': sys.path + ['modules'],
"packages":["os","sys","gi","random","subprocess","http.server","socketserver"],
"include_files":["files","img","ui.glade","files.json"]})
)
base = None
if sys.platform == "win32":
    base = "Win32GUI"
executables = [
    Executable('webserver.py', base=base),
    Executable('scpdatabase.py', base=base),
    Executable('search.py', base=base)]

setup(
    name = 'two exe in one folder',
    version = '0.2',
    description = 'Two exe in a single build folder',
    options = options,
    executables = executables
    )

