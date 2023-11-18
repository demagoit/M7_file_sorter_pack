from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='Sorts folder contain to dediicated subfolders',
    url='https://github.com/demagoit/M7_file_sorter_pack.git',
    author='demagoit',
    author_email='33demagoit@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=[],
    entry_points={'console_scripts': [
        'clean_folder = clean_folder.clean:main']}
)
