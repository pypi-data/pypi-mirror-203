from setuptools import setup, find_packages

setup(
    name='kilu',
    version='1.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'kilu=kilu:main_kilu',
            'dir2kilu=kilu:main_dir2kilu',
        ],
    },
    install_requires=[
        'PyYAML',
    ],
    author='Arturo "Buanzo" Busleiman',
    author_email='buanzo@buanzo.com.ar',
    description='Kilu: A YAML-based template system for generating project files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/buanzo/kilu',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
