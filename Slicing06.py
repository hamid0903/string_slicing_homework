def main(s,n):
    """
    The s string variable is given. return all characters except n characters from the beginning.
    Args:
        s(str): parameter
        n(int): parameter
    Returns:
        str: answer
    """
    s1=len(s)-(2*len(s))
    k=s1+n
    return s[k:]
print(main("samsung",2))