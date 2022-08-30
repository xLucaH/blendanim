"""
This script automatically creates all needed code and files to run a script using this animation package within
blender.
"""

import os
import textwrap


def create_files(blender_exe_path: str, working_dir: str):
    """
    Create an entry point script for running blender in a subprocess without manual setup.
    """

    script_write_path = os.path.join(working_dir, 'blender_script.py')

    content_main = f"""
    import subprocess

    subprocess_cmnds = ['{blender_exe_path}', '-d', '--python',
                        '{script_write_path}', '--', '{working_dir}']
    subprocess.call(subprocess_cmnds)
    """[1:]  # removing the first line break.

    write_path = os.path.join(working_dir, 'main.py')

    if os.name == 'nt':
        content_main = content_main.replace('\\', '\\\\')

    with open(write_path, 'w') as f:
        f.write(textwrap.dedent(content_main))

    content_script = f"""
    import sys
    # We need to append the working dir to the PYTHONPATH for blender to look inside our project's source folder
    working_dir = sys.argv[-1]
    print(working_dir)
    sys.path.append(working_dir)
    
    from src import entities, animation
    
    cube = entities.Cube(width=2, height=2)
    animate = animation.Animate(cube)

    animate.scale("x", 2, start=0, end=1000)
    """[1:]  # removing the first line break.

    with open(script_write_path, 'w') as f:
        f.write(textwrap.dedent(content_script))


def main():
    blender_exe_path = input('Please insert the absolute path of your blender executable file: ')
    working_dir = input('By default, we use the script\'s current execution path as the root folder.\nPress enter to '
                        'continue with this setting, or enter a new root folder path here: ')

    if working_dir == '':
        working_dir = os.getcwd()

    create_files(blender_exe_path, working_dir)

    print('Installation has been completed.\nRun "python main.py" to test out your first animation script.\nEdit '
          '"blender_script.py" to play around with the animation features.')


if __name__ == '__main__':
    main()
