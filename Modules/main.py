
import py_compile
import module
import compileall

py_compile.compile('Modules/module.py')
compileall.compile_dir('Modules')