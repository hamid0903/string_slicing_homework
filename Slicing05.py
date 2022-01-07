def main(s,n):
    """
    The s string variable is given. return n characters from the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s1=len(s)
    k=s1-n
    return s[k:]
print(main("samsung", 3))
