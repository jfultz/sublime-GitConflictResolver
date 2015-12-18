import os
import subprocess


def execute_command(command, working_dir=None):
    startupinfo = None
    stdpipe = None
    # hide console window on windows
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        stdpipe = subprocess.PIPE

    output = None
    try:
        output = subprocess.check_output(
            command,
            cwd=working_dir,
            startupinfo=startupinfo,
            stdin=stdpipe,
            stderr=stdpipe
        )
    except (subprocess.CalledProcessError, AttributeError):
        # Git will return an error when the given directory
        # is not a repository, which means that we can ignore this error
        pass
    else:
        output = str(output, encoding="utf-8").strip()

    return output
