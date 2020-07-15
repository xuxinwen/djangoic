import os
from importlib.machinery import SourceFileLoader


def import_submods(file, context):
    parent_dir = os.path.dirname(file)

    for filename in os.listdir(parent_dir):
        if not filename.startswith('_') and filename.endswith('.py'):
            full_filename = os.path.join(parent_dir, filename)
            if os.path.isfile(full_filename):
                mod_name, _ = os.path.splitext(filename)
                mod = SourceFileLoader(mod_name, full_filename).load_module()

                if hasattr(mod, '__all__'):
                    for attr in mod.__all__:
                        context[attr] = getattr(mod, attr)
                else:
                    for k, v in mod.__dict__.items():
                        if not k.startswith('_'):
                            context[k] = v
