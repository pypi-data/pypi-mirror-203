from setuptools import setup, Extension
from Cython.Build import cythonize


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="nazo_rand",
    ext_modules=cythonize(
        Extension(
            name="",
            sources=["nazo_rand/nazo_rand.pyx"],
            language=["c++"],
            extra_compile_args=["-std=c++17", "-O3"],
            extra_link_args=["-O3"],
        ),
        compiler_directives={
            "language_level": 3,
            "boundscheck": False,
            "wraparound": False,
            "binding": True,
            "cdivision": True,
        },
    ),
    author="bymoye",
    author_email="s3moye@gmail.com",
    version="0.0.6",
    description="A fast random number generator for python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license="Free for non-commercial use",
    package_data={
        "": [
            "nazo_rand/nazo_rand.pyi",
            "nazo_rand/nazo_rand.pyx",
            "nazo_rand/nazo_rand.hpp",
            "nazo_rand/nazo_rand.pxd",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Cython",
        "Programming Language :: C++",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    packages=["nazo_rand"],
)
