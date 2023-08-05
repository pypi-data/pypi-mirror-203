from setuptools import setup,  find_namespace_packages      # type: ignore
from glob import glob
from os.path import basename
from os.path import splitext

VERSION = {}

with open("./src/__init__.py") as fp:
    # pylint: disable=W0122
    exec(fp.read(), VERSION)

setup(
    name="redscrap",
    author="Martim Lima",
    author_email="martim.d.lima@protonmail.com",
    url='https://github.com/martimdLima',
    description='A brief synopsis of the project',
    long_description='A much longer explanation of the project and helpful resources',
    version=VERSION.get("__version__", "0.0.1"),
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src", exclude=["tests"]),
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    include_package_data=True,
    install_requires=[
        "click",
        "beautifulsoup4",
        "loguru",
        "requests",
        "httpx",
        "aiohttp",
        "validators",
        "DateTime",
        "colorama",
        "tqdm",
        "Pillow",
        "pytest",
        "pytest-cov",
        "pytest-mock",
        "setuptools",
    ],
    entry_points='''
        [console_scripts]
        redscrap=core.main:main
    ''',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.0",
        "Topic :: Utilities",
    ],
)




