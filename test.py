path = ""
def testString(path):
    path = path+" "+path
    print("in function:"+path)
if __name__ == "__main__":
    path = "some test"
    print("before function:"+path)
    testString(path)
    print("after function:"+path)