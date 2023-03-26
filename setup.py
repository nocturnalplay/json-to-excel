from cx_Freeze import setup, Executable

setup(
    name="JSON_EXCEL_Converter",
    version="1.0",
    description="this is the tool to convert JSON data into excel format conversion",
    executables=[Executable("app.py")],
)
