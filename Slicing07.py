def main(s,n):
    """
    The s string variable is given. return all characters except n characters at the end.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s1=len(s)
    k=s1-n
    return s[0:k]
print(main("samsung",2))