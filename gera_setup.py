import cx_Freeze

executables = [
    cx_Freeze.Executable(script="main.py", icon="assets/assets/icone.ico")
    ]

cx_Freeze.setup(
    name = "Corrida Maluca",
    options = {
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executables
)