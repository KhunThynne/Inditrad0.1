import argparse


# def argument_Set(arg_name:str,arg_short_name:str,help_description:str="",default:any=False):
#     parser.add_argument(f'-{arg_short_name}', f'--{arg_name}', default=default, help=help_description,required=False)
#     # parser.add_argument(f'-t', f'--test', default=default, help=help_description,required=False)


class argument_Set:
    def __init__(self, description:str="My programe argument.", prog:str="", epilog: str = "") -> None:
        self.parser = argparse.ArgumentParser(
            description=description, prog=prog, epilog=epilog)

    def argument_add(self, flags: any = None, help_description: str = "", default: any = False,
                     required=False, choices: list = [], nargs="?"):
        try:
            if isinstance(flags, list):
                self.parser.add_argument(f'{flags[0]}',
                                         f'{flags[1]}',
                                         default=default,
                                         help=help_description, required=required,
                                         )
            else:
                self.parser.add_argument(flags, help=help_description,
                                         choices=choices if choices else None, nargs=nargs, default=default)
        except TypeError as e:
            print(e)

    def argument_create(self):

        return self.parser.parse_args()
