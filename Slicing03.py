def main(s):
    """The s string variable is given. Return all characters except the one at the beginning and end.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    s1=len(s)
    k=s1-1
    return s[1:k]
print(main("samsung"))