"""
    Run all tests in web.py modules
"""
import webtest


def suite():
    modules = ["doctests", "auth"]
    return webtest.suite(modules)

if __name__ == "__main__":
    webtest.main()
