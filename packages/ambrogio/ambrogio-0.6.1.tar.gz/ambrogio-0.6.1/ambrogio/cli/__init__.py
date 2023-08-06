import os
from pathlib import Path
import signal

from ambrogio.cli.start import start
from ambrogio.cli.prompt import Prompt, ask_for_interrupt
from ambrogio.environment import get_closest_ini
from ambrogio.utils.project import create_project
from ambrogio.utils.threading import pause_event


available_commands = {
    'init': 'Create a new project',
    'create': 'Create a new procedure',
    'start': 'Start the project'
}


def signal_handler(signal, frame):
    """
    Handle SIGINT signal.
    It won't be handled if the pause_event is set, so the Prompt will be
    able to handle it.
    """

    if not pause_event.is_set():
        ask_for_interrupt()

    else:
        raise KeyboardInterrupt


def execute():
    """
    Run Ambrogio via command-line interface.
    """
    
    signal.signal(signal.SIGINT, signal_handler)

    if not get_closest_ini('.'):
        create = Prompt.confirm('No Ambrogio project found. Do you want to create one?')

        if create:
            project_name = Prompt.text('Type the project name')
            
            if project_name:
                create_project(project_name)

                project_path: Path = Path('.') / project_name
                os.chdir(project_path.resolve())

                start()

    else:
        start()