import os


def generate_files():
    cwd = os.getcwd()
    startup_file = open("led_startup.bat", "w+")
    startup_file.write("\"{}\" \"{}\"".format(cwd + "\\env\\Scripts\\pythonw.exe", cwd + "\\sunset_sunrise_startup.py"))
    startup_file.close()

    shutdown_file = open("led_shutdown.bat", "w+")
    shutdown_file.write("\"{}\" \"{}\"".format(cwd + "\\env\\Scripts\\pythonw.exe", cwd + "\\sunset_sunrise_shutdown.py"))
    shutdown_file.close()


if __name__ == "__main__":
    generate_files()
