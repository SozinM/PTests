*** Settings ***
Documentation                                                   Django versions PTest
#Library                                                         Selenium2Library
Library                                                         MyLibrary
*** Variables ***

*** Test Cases ***
User can open page
    [Documentation]                                             Check Django site avialable
    test title                                                  https://www.djangoproject.com/download/

Table has entries
    [Documentation]                                             Check there is 11 entyes in table
    test entries                                                https://www.djangoproject.com/download/

Propertly named table class
    [Documentation]                                             Check that table class is django-supported-versions
    test main table class                                       https://www.djangoproject.com/download/

Test red-marked entryes
    [Documentation]                                             Check that last 8 enries had class unsupported
    test unsupported class                                      https://www.djangoproject.com/download/

Test date logic
    [Documentation]                                             Check that date converted propertly and mainstream date < extended date
    test date logic                                             https://www.djangoproject.com/download/

Test version format
    [Documentation]                                             Check that version format is number splited by dot
    test versions numbers splitted by dots                      https://www.djangoproject.com/download/

Test version is numbers
    [Documentation]                                             Chech that version contains only numbers
    test versions numbers                                       https://www.djangoproject.com/download/

Test version logic
    [Documentation]                                             Check that Release Series it is a substring of Latest Release
    test versions substring                                     https://www.djangoproject.com/download/

*** Keywords ***

