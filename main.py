import importlib
from inspect import getmembers, isfunction

from tests import config

functions = dict()
for function_path in config.FUNCTION_PATHES:
    imported_module = importlib.import_module(function_path)

    for module_member in getmembers(imported_module):
        module_obj = module_member[1]
        if isfunction(module_obj) and hasattr(module_obj, 'mv_name'):
            function_key = '{}_{}'.format(module_obj.mv_name,
                                          module_obj.mv_version)
            functions[function_key] = module_obj

for function_info in config.PROCESSING_FUNCTIONS:
    function_key = '{}_{}'.format(function_info.get('name'),
                                  function_info.get('version'))

    function = functions.get(function_key)
    if function:
        result = function(config.PROCESSING_DATA)
        print(function_key, ':', result)
