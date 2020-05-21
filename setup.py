from cx_Freeze import Executable, setup
setup(name = 'Interactive Dictionary',
    version = '0.1',
    description = "Input any word and get the meaning of that word in "+
                    "English (JSON file is used)",
    executables = [Executable('interactive_dict.py')],
)

    