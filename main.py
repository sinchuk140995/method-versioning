import sys
import importlib
from inspect import getmembers, isfunction

from tests import config

functions = dict()
for function_path in config.FUNCTION_PATHES:
    try:
        imported_module = importlib.import_module(function_path)
    except ImportError:
        sys.stderr.write("No module named '{}'\n".format(function_path))
        exit(1)

    for module_member in getmembers(imported_module):
        module_obj = module_member[1]
        if isfunction(module_obj) and hasattr(module_obj, 'mv_name'):
            function_key = '{}_{}'.format(module_obj.mv_name,
                                          module_obj.mv_version)
            functions[function_key] = module_obj

for function_info in config.PROCESSING_FUNCTIONS:
    function_key = '{}_{}'.format(function_info.get('name'),
                                  function_info.get('version'))

    try:
        function = functions[function_key]
    except KeyError:
        error = "Function '{}' version {} wasn't found.\n".format(function_info.get('name'),
                                                                  function_info.get('version'))
        sys.stderr.write(error)
        exit(1)

    function_result = function(*config.PROCESSING_DATA['args'], **config.PROCESSING_DATA['kwargs'])
    result_message = "Function '{}' version {} result: {}\n".format(function_info.get('name'),
                                                                    function_info.get('version'),
                                                                    function_result)
    sys.stdout.write(result_message)
