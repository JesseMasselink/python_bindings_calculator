""" Task definitions for invoke command line utility for python bindings
    overview article.
"""
import cffi
import invoke
import pathlib
import sys
import os
import shutil
import re
import glob

on_win = sys.platform.startswith("win")


@invoke.task
def clean(c):
    """Remove any built objects"""
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd",
        "cffi_example*",  # Is this a dir?
        "cython_wrapper.cpp",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)
    for dir_pattern in "Release":
        for dir in glob.glob(dir_pattern):
            shutil.rmtree(dir)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))

@invoke.task()
def build_cppfunc(c):
    """Build the shared library for the sample C++ code"""
    print_banner("Building C++ Library")
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppfunc.cpp "
        "-o libcppfunc.so "
    )
    print("* Complete")
#
# @invoke.task()
# def build_cppadd(c):
#     """Build the shared library for the sample C++ code"""
#     print_banner("Building C++ Library")
#     invoke.run(
#         "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppadd.cpp "
#         "-o libcppadd.so "
#     )
#     print("* Complete")
#
# @invoke.task()
# def build_cppsub(c):
#     """Build the shared library for the sample C++ code"""
#     print_banner("Building C++ Library")
#     invoke.run(
#         "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppsub.cpp "
#         "-o libcppsub.so "
#     )
#     print("* Complete")
#
# @invoke.task()
# def build_cppmult(c):
#     """Build the shared library for the sample C++ code"""
#     print_banner("Building C++ Library")
#     invoke.run(
#         "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppmult.cpp "
#         "-o libcppmult.so "
#     )
#     print("* Complete")
#
# def build_cppdiv(c):
#     """Build the shared library for the sample C++ code"""
#     print_banner("Building C++ Library")
#     invoke.run(
#         "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppdev.cpp "
#         "-o libcppdev.so "
#     )
#     print("* Complete")
# @invoke.task()
# def build_cppfib(c):
#     """Build the shared library for the sample C++ code"""
#     print_banner("Building C++ Library")
#     invoke.run(
#         "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppfib.cpp "
#         "-o libcppfib.so "
#     )
#     print("* Complete")

def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
        "`python3 -m pybind11 --includes` "
        "-I . "
        "{0} "
        "-o {1}`python3-config --extension-suffix` "
        "-L. -lcppfunc -Wl,-rpath,.".format(cpp_name, extension_name)
        #"-L. -lcppadd -lcppsub -lcppmult -Wl,-rpath,.".format(cpp_name, extension_name)
    )

@invoke.task(build_cppfunc) #build_cppsub, build_cppadd, build_cppmult
def build_pybind11(c):
    """Build the pybind11 wrapper library"""
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_wrapper.cpp", "pybind11_example")
    print("* Complete")


@invoke.task(build_pybind11)
def test_pybind11(c):
    """Run the script to test PyBind11"""
    print_banner("Testing PyBind11 Module")
    invoke.run("python3 pybind11_test.py", pty=True)

@invoke.task(
    clean,
    build_cppfunc,
    build_pybind11,
    test_pybind11,
)
def all(c):
    """Build and run all tests"""
    pass
