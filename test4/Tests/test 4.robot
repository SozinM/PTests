*** Settings ***
Documentation                                                   Django versions PTest
#Library                                                         Selenium2Library
Library                                                         MyLibrary


*** Variables ***
${Tagret site}                                                  https://www.djangoproject.com/download/
${Site title}                                                   Download Django | Django
${Table class}                                                  django-supported-versions
${Unsupported class}                                            unsupported


*** Test Cases ***
User can open page
    [Documentation]                             Check Django site avialable
    test title                                  ${Tagret site}    ${Site title}

Table has entries
    [Documentation]                             Check there is 11 entyes in table
    test entries                                ${Tagret site}

Propertly named table class
    [Documentation]                             Check that table class is django-supported-versions
    test main table class                       ${Tagret site}    ${Table class}

Test red-marked entryes
    [Documentation]                             Check that last 8 enries had class unsupported
    test unsupported class                      ${Tagret site}    ${Unsupported class}

Test date logic
    [Documentation]                             Check that date converted propertly and mainstream date < extended date
    test date logic                             ${Tagret site}

Test version format
    [Documentation]                             Check that version format is number splited by dot
    test versions numbers splitted by dots      ${Tagret site}

Test version is numbers
    [Documentation]                             Chech that version contains only numbers
    test versions numbers                       ${Tagret site}

Test version logic
    [Documentation]                             Check that Release Series it is a substring of Latest Release
    test versions substring                     ${Tagret site}


*** Keywords ***

