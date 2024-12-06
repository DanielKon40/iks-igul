
"""Using cx_Freeze"""

from cx_Freeze import setup, Executable

setup(
    name="IKS_IGUL",
    version="1.0",
    description="Description of your app",
    executables=[Executable("main.py")]
)

