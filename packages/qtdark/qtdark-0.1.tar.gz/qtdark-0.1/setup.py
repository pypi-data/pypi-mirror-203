from setuptools import setup, find_packages

setup(
    name='qtdark',
    version='0.1',
    author='Tat Nguyen Van',
    author_email='nguyenvantat1182002@gmail.com',
    url='https://github.com/nguyenvantat1182002/qtdark',
    packages=find_packages(),
    install_requires=[
        'pyqt5-tools',
        'pyqt5'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)