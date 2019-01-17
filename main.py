import sys
import importlib
from inspect import getmembers, isfunction


try:
    config_index = sys.argv.index('--config') + 1
except ValueError:
    sys.stderr.write("Please, provide a --config parameter\n")
    exit(1)

try:
    config_path = sys.argv[config_index]
except IndexError:
    sys.stderr.write("Please, provide a config file path in dot notation.\n")
    exit(1)

try:
    config = importlib.import_module(config_path)
except ImportError:
    sys.stderr.write("Config file '{}' not found\n".format(config_path))
    exit(1)

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

result = None
for function_info in config.PIPELINE_FUNCTIONS:
    function_key = '{}_{}'.format(function_info.get('name'),
                                  function_info.get('version'))

    try:
        function = functions[function_key]
    except KeyError:
        error = "Function '{}' version {} wasn't found.\n".format(function_info.get('name'),
                                                                  function_info.get('version'))
        sys.stderr.write(error)
        exit(1)

    if result is None:
        result = function(**config.DATA)
    else:
        result = function(result)

    result_message = "Function '{}' version {} result: {}\n".format(function_info.get('name'),
                                                                    function_info.get('version'),
                                                                    result)
    sys.stdout.write(result_message)
