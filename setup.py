import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ["data/"]
packages = [""]

target = Executable(
    script="C42 Toollist Converter.py",
    base="Win32GUI",
    icon="data/favicon.ico"
)

# SETUP CX FREEZE
setup(
    name="C42 Toollist Converter",
    version="0.6",
    description="",
    author="Buecherl M.",
    options={'build_exe': {'include_files': files}},
    executables=[target]
)