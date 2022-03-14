import ast
import difflib
import importlib
import inspect
import sys
import textwrap
from types import ModuleType

REPLACE_ATTRS = frozenset({'name', 'id', 'arg', 'attr'})
RATIO = 0.95


def analyze_module(module: ModuleType, module_name: str) -> dict:
    res = {}

    ins = inspect.getmembers(module)
    for name, content in filter(lambda name_content: not (inspect.isclass(name_content[1]) and name_content[0].startswith("__")), ins):
        true_name = '.'.join((module_name, name))
        if inspect.isclass(content):
            # Анализируем класс
            pass
            res.update(**analyze_module(content, true_name))
        elif inspect.isfunction(content):
            code = textwrap.dedent(inspect.getsource(content))
            tree = ast.parse(code)
            for x in ast.walk(tree):
                for attr in REPLACE_ATTRS:
                    if hasattr(x, attr):
                        setattr(x, attr, '_')
            res.update({true_name: ast.unparse(tree)})
    return res


def compare_parsed_modules(m1: dict, m2: dict):
    d = {**m1, **m2}
    for i, (name_1, code_1) in enumerate(d.items()):
        for name_2, code_2 in list(d.items())[i + 1:]:
            if name_1 == name_2:
                continue
            if difflib.SequenceMatcher(a=code_1, b=code_2).ratio() >= RATIO:
                print(f"{name_1} {name_2}")


if __name__ == "__main__":
    args = sys.argv[1:]
    module_1 = args[0]
    module_2 = args[1] if len(args) > 1 else module_1
    d1 = analyze_module(importlib.import_module(module_1), module_1)
    d2 = analyze_module(importlib.import_module(module_2), module_2)
    compare_parsed_modules(d1, d2)
