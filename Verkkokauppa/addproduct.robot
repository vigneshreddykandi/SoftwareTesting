*** Settings ***
| Library | SeleniumLibrary


*** Keywords ***


*** Test Cases ***
Test adding product
    Open Browser    https://www.verkkokauppa.com/   (executable_path='C:/path/to/chromedriver.exe')
    Maximize Browser Window
    Sleep    3s
    Page Should Contain    Tuotealueet


    Click Element    name:query
    Input Text    name:query    koiranruoka
    Sleep    3s
    Click Button    name:submit

    Sleep    5s
    Page Should Contain    Lisää ostoskoriin
    
    Click Button    xpath:/html/body/div[1]/div[1]/div/div/main/div/div[2]/div/ol/li/article/div/div[1]/div/div[2]/div/button
    Sleep    3s
    Page Should Contain    Siirry kassalle
    Click Element    id:checkout
    Page Should Contain    1 tuote, yhteensä


    
Test 