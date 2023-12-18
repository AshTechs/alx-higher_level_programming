def safe_print_list(my_list, x=0):
    """
    Prints the elements of a list safely, avoiding IndexError.
    """
    for i in range(x):
        try:
            print(my_list[i], end="")
        except IndexError:
            break
    print("")
