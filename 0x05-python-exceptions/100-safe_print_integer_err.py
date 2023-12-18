#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{}".format(value).strip())
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
