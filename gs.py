# Open each result of Google-Searching in a new webbrowser tab
import argparse
import os
import sys
import webbrowser

from googlesearch import search

user_path = os.getenv('LOCALAPPDATA')
user_path = user_path.replace('\\', '/')
opera_exe = user_path + '/Programs/Opera/launcher.exe %s'

browsers = [{'name': 'chrome',
             'exe': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'},
            {'name': 'firefox',
             'exe': 'C:/Program Files/Mozilla Firefox/firefox.exe %s'},
            {'name': 'edge',
                'exe': 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'},
            {'name': 'opera',
             'exe': opera_exe}]

search_result = []
parser = argparse.ArgumentParser(
    description='Search in Google and open tabs')


def get_program_args(parser):
    parser.add_argument(
        'search_for', type=str, help='A search string for searching at Google')
    parser.add_argument('-b', '--browser', type=str, choices=['chrome', 'firefox', 'edge', 'opera'],
                        default='chrome', help='Which browser')
    parser.add_argument('-a', '--amount', type=int,
                        default=10, help='amount of webbrowser-tabs to open')
    # Read arguments from command line
    return parser.parse_args()


def get_browser_exe(browser: str) -> str:
    d = next(item for item in browsers if item['name'] == browser)
    return d['exe']


def do_search(program_args) -> list:
    number_of_results = program_args.amount
    searchResult = list(search(program_args.search_for, num=number_of_results, stop=number_of_results, pause=2)
                        )  # convert the generator to a list
    for i in searchResult:
        print(i)

    return searchResult


def open_browser_tabs(specific_browser: str):
    num_tabs = min(10, len(search_result))
    browser_exe = get_browser_exe(args.browser)
    print("Open each result in a new webbrowser tab...")

    for i in range(num_tabs):
        if i == 0:
            webbrowser.get(
                browser_exe).open_new(search_result[i])
        else:
            webbrowser.get(
                browser_exe).open_new_tab(search_result[i])


args = get_program_args(parser)
search_result = do_search(args)
open_browser_tabs(args.browser)
