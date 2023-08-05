import ctypes
import json
import os.path
import subprocess
import sys
from functools import wraps
import ast
import pandas as pd
from flatten_any_dict_iterable_or_whatsoever import fla_tu
from more_itertools import chunked
import numpy as np

config = sys.modules[__name__]
config.parsed_signatures = {}


def get_variables(func_name, file_path):
    r"""
    Given a function name and a file path, this function returns a list of tuples containing the names and values of all
    variables defined within the function.

    :param func_name: The name of the function to search for.
    :type func_name: str
    :param file_path: The path to the file containing the function.
    :type file_path: str
    :return: A list of tuples containing the names and values of all variables defined within the function.
    :rtype: List[Tuple[str, Any]]
    :raises ValueError: If the specified function is not found in the specified file.
    """
    with open(file_path, "r") as f:
        source = f.read()
    tree = ast.parse(source)
    func_def = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            func_def = node
            break
    if not func_def:
        raise ValueError(f"Function {func_name} not found in {file_path}")
    var_names = []
    var_values = []
    for node in ast.walk(func_def):
        if (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
        ):
            var_name = node.targets[0].id
            var_value = ast.literal_eval(node.value)
            var_names.append(var_name)
            var_values.append(var_value)
    return list(zip(var_names, var_values))


def nparray_right_dtype_conti(a, dtype):
    if not a.dtype == dtype:
        a = a.astype(dtype)
    if not a.flags["C_CONTIGUOUS"]:
        a = np.ascontiguousarray(a)
    return a


def formatctypes(parsedv, varstopass):
    r"""
    Converts variables in varstopass dictionary to ctypes data types based on their corresponding parsedv types.

    Args:
    - parsedv: A list of tuples containing variable names and their corresponding types.
    - varstopass: A dictionary containing variable names and their corresponding values.

    Returns:
    - arg_types: A dictionary containing variable names and their corresponding ctypes data types.
    """
    arg_types = {}
    for arg_name, arg_type in parsedv:
        if arg_type == "char":
            arg_types[arg_name] = ctypes.c_ubyte(varstopass[arg_name])

        elif arg_type == "char *":
            arg_types[arg_name] = np.frombuffer(
                varstopass[arg_name], dtype=np.uint8
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))

        if arg_type == "signed char":
            arg_types[arg_name] = ctypes.c_byte(varstopass[arg_name])

        elif arg_type == "signed char *":
            arg_types[arg_name] = np.frombuffer(
                varstopass[arg_name], dtype=np.int8
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_byte))

        elif arg_type == "unsigned char":
            arg_types[arg_name] = ctypes.c_ubyte(varstopass[arg_name])

        elif arg_type == "unsigned char *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.uint8
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))

        elif arg_type == "double":
            arg_types[arg_name] = ctypes.c_double(varstopass[arg_name])

        elif arg_type == "double *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.float64
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_double))

        elif arg_type == "float":
            arg_types[arg_name] = ctypes.c_float(varstopass[arg_name])

        elif arg_type == "float *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.float32
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_float))

        elif arg_type == "int":
            arg_types[arg_name] = ctypes.c_int(varstopass[arg_name])

        elif arg_type == "int *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.int32
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_int))

        elif arg_type == "long":
            arg_types[arg_name] = ctypes.c_long(varstopass[arg_name])

        elif arg_type == "long *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="long"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_long))

        elif arg_type == "longlong":
            arg_types[arg_name] = ctypes.c_longlong(varstopass[arg_name])

        elif arg_type == "longlong *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="longlong"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_longlong))

        elif arg_type == "short":
            arg_types[arg_name] = ctypes.c_short(varstopass[arg_name])

        elif arg_type == "short *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="short"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_short))

        elif arg_type == "str":
            arg_types[arg_name] = ctypes.c_char_p(varstopass[arg_name])

        elif arg_type == "str *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.str_
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_char_p))

        elif arg_type == "uint":
            arg_types[arg_name] = ctypes.c_uint(varstopass[arg_name])

        elif arg_type == "uint *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.uint
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_uint))

        elif arg_type == "ulong":
            arg_types[arg_name] = ctypes.c_ulong(varstopass[arg_name])

        elif arg_type == "ulong *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="ulong"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ulong))

        elif arg_type == "ulonglong":
            arg_types[arg_name] = ctypes.c_ulonglong(varstopass[arg_name])

        elif arg_type == "ulonglong *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="ulonglong"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ulonglong))

        elif arg_type == "ushort":
            arg_types[arg_name] = ctypes.c_ushort(varstopass[arg_name])

        elif arg_type == "ushort *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="ushort"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ushort))

        elif arg_type == "bool":
            arg_types[arg_name] = ctypes.c_bool(varstopass[arg_name])

        elif arg_type == "bool *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.bool_
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_bool))

        elif arg_type == "byte":
            arg_types[arg_name] = ctypes.c_byte(varstopass[arg_name])

        elif arg_type == "byte *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="byte"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_byte))

        elif arg_type == "ubyte":
            arg_types[arg_name] = ctypes.c_ubyte(varstopass[arg_name])

        elif arg_type == "ubyte *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype="ubyte"
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))

        elif arg_type == "wchar":
            arg_types[arg_name] = ctypes.c_wchar(varstopass[arg_name])

        elif arg_type == "wchar *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.unicode_
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_wchar))

        elif arg_type == "size_t":
            arg_types[arg_name] = ctypes.c_size_t(varstopass[arg_name])

        elif arg_type == "size_t *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.uintp
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_size_t))

        elif arg_type == "void_p":
            arg_types[arg_name] = ctypes.c_void_p(varstopass[arg_name])

        elif arg_type == "void_p *":
            arg_types[arg_name] = nparray_right_dtype_conti(
                varstopass[arg_name], dtype=np.void
            ).ctypes.data_as(ctypes.POINTER(ctypes.c_void_p))

    return arg_types


def ccoo(f_py=None):
    """
    Compiles a given Python function into a shared library using Clang and returns a decorator that can be used to
    replace the original function with the compiled version.

    :param f_py: The Python function to be compiled.
    :type f_py: Optional[Callable]
    :return: A decorator that can be used to replace the original function with the compiled version.
    :rtype: Callable
    :raises AssertionError: If the input function is not callable or None.
    """
    assert callable(f_py) or f_py is None
    compiledfunctionname = "__compiledctypesfunction_" + f_py.__name__

    f = sys._getframe(1)
    if not f.f_globals.get(compiledfunctionname):
        dct = f.f_globals
        csou = {
            x[0]: x[1]
            for x in (get_variables(f_py.__name__, dct.get("__file__", "")))
            if x[0] in ["c_save_path", "c_source_code"]
        }
        clangexe = dct.get("clangpath")
        csource = csou.get("c_source_code")
        wpa = os.path.normpath(
            os.path.join(os.path.dirname(sys.executable), csou["c_save_path"])
        )
        savepathso = os.path.normpath(wpa)
        commandsub = [
            clangexe,
            "-xc",
            "-O2",
            "-Wl,",
            "-out-implib,libCloop.dll.a",
            "-shared",
            "-o",
            savepathso,
            "-",
        ]
        olddict = os.getcwd()
        os.chdir(os.path.dirname(clangexe))
        paxas = subprocess.run(
            commandsub,
            input=csource.encode(),
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )

        cta = ctypes.cdll.LoadLibrary(savepathso)
        f.f_globals.__setitem__(compiledfunctionname, getattr(cta, f_py.__name__))
        data = subprocess.run(
            [clangexe, "-xc", "-Xclang", "-ast-dump=json", "-fsyntax-only", "-"],
            input=csource.encode(),
            capture_output=True,
            shell=True,
        ).stdout

        da = list(fla_tu(json.loads(data)))
        os.chdir(olddict)
        df = pd.DataFrame(da)
        xx2 = df.loc[df[1].apply(lambda x: x[-1] in ["name", "qualType"])]
        xx2 = xx2[xx2.index.get_loc(xx2.loc[xx2[0] == f_py.__name__].index[0]) + 1 :]
        general = xx2.iloc[0][0]
        xx2 = xx2[1:]
        totallen = len(general.split(", "))
        xx3 = xx2[: totallen * 2][0].to_list()
        xx3 = list(chunked(xx3, 2))
        config.parsed_signatures[f_py.__name__] = xx3.copy()

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            arg_types = formatctypes(
                config.parsed_signatures[f_py.__name__], varstopass=kwargs
            )
            arg_typeslist = [x[1] for x in arg_types.items()]

            vala = f.f_globals[compiledfunctionname](*args, *arg_typeslist)
            return vala

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
