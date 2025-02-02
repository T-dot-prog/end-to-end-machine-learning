from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REPO_NAME = 'End-to-End-machine-learning-project'
AUTHOR_USER_NAME= 'T-dot-prog'
SRC_REPO= 'machine_learning_project'
AUTHOR_EMAIL = 'tahasinahoni2@gmai.com'

setup(
    name=REPO_NAME,
    version='0.0.0',
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='An end-to-end machine learning project.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/{}/{}'.format(AUTHOR_USER_NAME, REPO_NAME),
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir={"":"src"},
    packages= find_packages(where= 'src')
)
