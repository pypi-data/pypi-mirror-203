import argparse

parser = argparse.ArgumentParser(description='Create a new project with QtDark.')
parser.add_argument('create-app', type=str, help='project name.')

args = parser.parse_args()
project_name = args['create-app']
print(project_name)