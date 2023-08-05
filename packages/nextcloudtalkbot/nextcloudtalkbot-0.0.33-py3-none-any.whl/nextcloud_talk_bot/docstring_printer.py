import argparse
import importlib
import inspect


class DocstringPrinter:
    """
    A class for printing the docstrings of classes and methods from specified modules.

    :param input_name: The name of the input used to map to a module.
    :param base_url: The base URL of your Nextcloud instance (optional).
    :param username: Your Nextcloud username (optional).
    :param password: Your Nextcloud password (optional).
    :param room_name: The name of the Nextcloud Talk room (optional).
    """

    def __init__(
            self,
            input_name,
            base_url=None,
            username=None,
            password=None,
            room_name=None):
        self.module_name = self.map_input_to_module(input_name)
        self.base_url = base_url
        self.username = username
        self.password = password
        self.room_name = room_name
        self.load_module()

    def map_input_to_module(self, input_name):
        mapping = {
            "activities": "nextcloud_activities",
            "user": "nextcloud_user",
            "file": "nextcloud_file_operations",
            "meeting": "nextcloud_meeting",
            "messages": "nextcloud_messages",
            "poll": "nextcloud_poll",
            "requests": "nextcloud_requests",
            "extractor": "nextcloud_talk_extractor",
            "talkbot": "Nextcloudtalkbot",
        }
        return mapping.get(input_name, input_name)

    def load_module(self):
        self.module = importlib.import_module(self.module_name)

    def get_first_class(self):
        for name, obj in inspect.getmembers(self.module):
            if inspect.isclass(obj) and obj.__module__ == self.module_name:
                return obj
        return None

    def print_first_class_docstring(self):
        cls = self.get_first_class()
        if cls:
            docstring = inspect.getdoc(cls)
            if docstring:
                print(f"{docstring}\n")
            else:
                print(f"{cls.__name__} has no docstring.")
        else:
            print(f"No classes found in module {self.module_name}.")

    def print_method_docstring(self, method_name):
        cls = self.get_first_class()
        if cls:
            method = getattr(cls, method_name, None)
            if method:
                docstring = inspect.getdoc(method)
                if docstring:
                    print(f"{docstring}\n")
                else:
                    print(f"Method '{method_name}' has no docstring.")
            else:
                print(
                    f"Method '{method_name}' not found in class '{cls.__name__}'.")
        else:
            print(f"No classes found in module {self.module_name}.")

    def call_class_method(self, method_name, *args, **kwargs):
        if len(list(args)) > 1:
            args_list = list(args)
            first = args_list.pop(0)
            if "[" in args_list:
                nargs = args_list[1]
        else:
            nargs = args
            first = None
        cls = self.get_first_class()
        if cls:
            instance = cls(
                self.base_url,
                self.username,
                self.password,
                self.room_name)
            method = getattr(instance, method_name, None)
            if method:
                return method(first, nargs)
            else:
                print(
                    f"Method '{method_name}' not found in class '{cls.__name__}'.")
        else:
            print(f"No classes found in module {self.module_name}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Call a method of the first class in the specified module or print its docstring.",
        add_help=False)
    parser.add_argument(
        "input_name",
        help="Name of the input to map to a module.")
    parser.add_argument(
        "--method",
        dest="method_name",
        default=None,
        help="Method name to call.")
    parser.add_argument(
        "--args",
        nargs="*",
        default=[],
        help="Arguments to pass to the method.")
    parser.add_argument(
        "--help",
        dest="help_flag",
        action="store_true",
        help="Print class docstring.")
    parser.add_argument(
        "--base_url",
        required=False,
        help="Base URL for Nextcloud instance.")
    parser.add_argument(
        "--username",
        required=False,
        help="Username for Nextcloud.")
    parser.add_argument(
        "--password",
        required=False,
        help="Password for Nextcloud.")
    parser.add_argument(
        "--room_name",
        required=False,
        help="Nextcloud Talk room name.")

    args = parser.parse_args()

    docstring_printer = DocstringPrinter(
        args.input_name,
        args.base_url,
        args.username,
        args.password,
        args.room_name)
    if args.help_flag:
        if args.method_name:
            docstring_printer.print_method_docstring(args.method_name)
        else:
            docstring_printer.print_first_class_docstring()
    elif args.method_name:
        result = docstring_printer.call_class_method(
            args.method_name, *args.args)
        if result:
            print(f"Result: {result}")
    else:
        parser.print_help()
