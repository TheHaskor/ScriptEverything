from inspect import isfunction

import webbrowser
chrome_path = r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"


def SE_help():
    def print_function(function_key, func):
        if isfunction(func):
            doc = func.__doc__
            if doc:
                if doc.startswith('SE:'):
                    print(f'{function_key}: {doc[2:]}')
    for function_key, func in globals().items():
        print_function(function_key, func)


def print_something():
    """SE: prints something to screen"""
    print('something')


def work(browser='chrome'):
    """SE: quickly opens work tabs"""
    work_urls = ['https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python',
            'https://github.com/',
            'http://10.0.2.65:8080/']
    open_urls(browser, work_urls)


def open_urls(browser, urls):
    webbrowser.register(browser, None, webbrowser.BackgroundBrowser(chrome_path))
    for url in urls:
        webbrowser.open_new_tab(url)

