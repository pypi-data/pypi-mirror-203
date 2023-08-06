import os
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create QtDark project.')
    parser.add_argument('name', type=str, help='project name.')

    args = parser.parse_args()
    project_name = args.name
    package_dir = os.path.dirname(os.path.abspath(__file__))

    shutil.copy2(
        src=f'{package_dir}\\init.py',
        dst=f'{os.getcwd()}\\{project_name}.py'
    )

    shutil.copy(
        src=f'{package_dir}\\program.py',
        dst=os.getcwd()
    )