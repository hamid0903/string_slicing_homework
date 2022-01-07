def main(s):
    """
    The s string variable is given. return four characters from the end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1=len(s)
    k=s1-4
    return s[k:]
print(main("samsung"))