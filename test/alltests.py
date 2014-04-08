import webtest

def suite():
    modules = ["auth"]
    return webtest.suite(modules)

if __name__ == "__main__":
    webtest.main()
