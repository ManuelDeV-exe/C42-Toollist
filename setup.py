import sys
import os
from cx_Freeze import setup, Executable

# Build Optionen
build_exe_options = dict(packages = ["pathlib", "PySide6", "sys", "os"], excludes = [], include_files = ["data/", "platforms/"])

# Ziel
target = Executable(
    script="C42-Toollist.py",
    base="Win32GUI",
    icon="data/favicon.ico"
)

# Setup CX Freez
setup( 
    name = "C42 Toollist",
    version = "0.1",
    description = "Umwaandeln der Spannlisten",
    author= "Manuel Bücherl",
    options = {'build_exe' : build_exe_options},
    executables = [target]
    )