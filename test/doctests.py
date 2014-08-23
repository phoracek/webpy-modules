"""
    Run all doctests in web.py modules
"""
import webtest


def suite():
    modules = [
        "webmod.utils",
    ]
    return webtest.doctest_suite(modules)

if __name__ == "__main__":
    webtest.main()
