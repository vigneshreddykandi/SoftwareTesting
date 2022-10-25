// vignesh reddy kandi

*** Settings ***
Library    OperatingSystem
Library    Collections
Library    String

*** Test Cases ***
Get text file
    ${addresses}=    Get File    webpages.txt
    @{addresses}=    Split String    ${addresses}
    Set global variable    ${addresses}

Ping webpages on text file
    # Loops through the adresses
    FOR    ${element}    IN    @{addresses}
        
        # Gets the output
        @{return}=    Run And Return Rc And Output    ping ${element}

        # Appends the Ip adress and Information about the pinging
        ${string}=     Convert To String    @{return}[1:2]
        ${line}=    Get Line    @{return}[1:2]    1
        Append To File    return.txt    ${line} ${\n}
        ${line}=    Get Line    @{return}[1:2]    -1
        Append To File    return.txt    ${line} ${\n}

        # Gets the average time
        @{split}=    Split String    ${line}
        ${time}=    Get Substring    @{split}[8:9]    0    2
        
        ${time}=    Convert To Integer    ${time}
        
        # Average time should be less than 50 ms
        Should Be True    ${time} < 50

    END
