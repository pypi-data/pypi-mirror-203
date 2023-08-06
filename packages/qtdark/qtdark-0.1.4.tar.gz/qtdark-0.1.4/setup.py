from setuptools import setup, find_packages

setup(
    name='qtdark',
    version='0.1.4',
    description='Create QtDark project.',
    author='Tat Nguyen Van',
    author_email='nguyenvantat1182002@gmail.com',
    url='https://github.com/nguyenvantat1182002/SeleneXtra',
    packages=find_packages(),
    install_requires=[
        'pyqt5-tools',
        'pyqt5'
    ],
    entry_points={
        'console_scripts': [
            'qtdark=qtdark.__main__:main'
        ]
    }
)
