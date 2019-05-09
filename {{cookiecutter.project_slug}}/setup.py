#!/usr/bin/env python
from typing import List

from pip._internal.download import PipSession
from pip._internal.req import parse_requirements
from setuptools import find_packages, setup


def load_requirements(path: str) -> List[str]:
    install_reqs = parse_requirements(path, session=PipSession())
    return [str(ir.req) for ir in install_reqs]


requirements = load_requirements('requirements/concrete/requirements.txt')
test_requirements = load_requirements('requirements/concrete/requirements.test.txt')
setup_requirements = load_requirements('requirements/concrete/requirements.setup.txt')

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='{{ cookiecutter.project_slug }}',
    use_scm_version=True,
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='{{ cookiecutter.project_slug }}',
    url='https://gitlab.com/{{ cookiecutter.username }}/{{ cookiecutter.project_slug }}',
    license="MIT License",

    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',

    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require={
        'testing': test_requirements,
    },

    entry_points={
        'console_scripts': [
            # example:
            # 'name=dotted.module.path:function_name',
        ],
    },

    python_requires=">=3.5",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    test_suite='tests',
    zip_safe=False,
    include_package_data=True,
)
