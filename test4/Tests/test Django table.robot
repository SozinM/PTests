*** Settings ***
Documentation                                   Django versions PTest
Library                                         MyLibrary
Test Setup                                      Open django page
Test Teardown                                   Close django page

*** Variables ***
${Tagret site}                                  https://www.djangoproject.com/download/
${Site title}                                   Download Django | Django
${Table class}                                  django-supported-versions
${Unsupported class}                            unsupported


*** Test Cases ***
User can open page
    [Documentation]                             Check Django site avialable
    test title                                  ${Site title}

Table has entries
    [Documentation]                             Check there is 11 entyes in table
    test entries

Propertly named table class
    [Documentation]                             Check that table class is django-supported-versions
    test main table class                       ${Table class}

Test red-marked entryes
    [Documentation]                             Check that last 8 enries had class unsupported
    test unsupported class                      ${Unsupported class}

Test date logic
    [Documentation]                             Check that date converted propertly and mainstream date < extended date
    test date logic

Test version format
    [Documentation]                             Check that version format is number splited by dot
    test versions numbers splitted by dots

Test version is numbers
    [Documentation]                             Chech that version contains only numbers
    test versions numbers

Test version logic
    [Documentation]                             Check that Release Series it is a substring of Latest Release
    test versions substring


*** Keywords ***
Open django page
    open browser  https://www.djangoproject.com/download/

Close django page
    close browser
