import os
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create QtDark project.')
    parser.add_argument('name', type=str, help='project name.')

    args = parser.parse_args()
    project_name = args.name
    base_folder = f'{os.getcwd()}\\qtdark'

    shutil.copy2(
        src=f'{base_folder}\\init.py',
        dst=f'{os.getcwd()}\\{project_name}.py'
    )

    shutil.copy(
        src=f'{base_folder}\\program.py',
        dst=os.getcwd()
    )