import os
import shutil
import argparse

def main():
    parser = argparse.ArgumentParser(description='Create a new project with QtDark.')
    parser.add_argument('name', type=str, help='project name.')

    args = parser.parse_args()
    project_name = args.name

    shutil.copy2(f'qtdark/init.py', f'{os.getcwd()}\\{project_name}.py')
    shutil.copy(f'qtdark/program.py', os.getcwd())

if __name__ == '__main__.py':
    main()