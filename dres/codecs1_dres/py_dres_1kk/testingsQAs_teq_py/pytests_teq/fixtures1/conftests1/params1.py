""" global params for this app; eg: for cmdline args,... """

cmdline_args_names: list = ['--arg1', '--arg2',]   # - args-identifiers/names, as later on shell-cmdline: pytest --arg1=xxx ...
cmdline_args: dict = {}
for name1 in cmdline_args_names:
    cmdline_args[name1] = f"param1_{name1}"   # -set default values for args

