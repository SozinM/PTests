*** Settings ***
Documentation                                   Django versions PTest
Library                                         MyLibrary
Test Setup                                      Open page
Test Teardown                                   Close page

*** Variables ***
${Tagret site}                                  https://www.djangoproject.com/download/
${Site title}                                   Download Django | Django
${Table class}                                  django-supported-versions
${Unsupported class}                            unsupported


*** Test Cases ***
User can open page
    [Documentation]                             Check Django site avialable NOTE: this is useless for our test target\
    ...                                         Tags: useless
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
    [Documentation]                             Check that date converted propertly and mainstream date < extended date\
    ...                                         Tags: critical
    test date logic

Test version format
    [Documentation]                             Check that version format is number splited by dot\
    ...                                         Tags: critical
    test versions numbers splitted by dots

Test version is numbers
    [Documentation]                             Chech that version contains only numbers\
    ...                                         Tags: critical
    test versions numbers

Test version logic
    [Documentation]                             Check that Release Series it is a substring of Latest Release\
    ...                                         Tags: critical
    test versions substring


*** Keywords ***
Open page
    open browser                                ${Tagret site}

Close page
    close browser
