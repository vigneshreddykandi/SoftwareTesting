*** settings ***
Library  DatabaseLibrary
Library  OperatingSystem
Library  pymysql

*** Variables ***
${DBName}   RobotFramework
${DBUser}   Robot
${DBPassword}  password
${DBHost}    127.0.0.1
${DBPort}    3306

*** Test Cases ***

Inserting Data to module table
Connect DB
${output} =  Execute Sql String  INSERT INTO "robotframework."module("Textt." Number". "Date")VALUES ("Text2", 2, '2008-05-09")
Should Be Equal As Strings ${output} None

Deleting Data from module table
Connect DB
${output} = Execute Sql String DELETE FROM 'robotframework."module' where idmodule=4:
Should Be Equal As Strings ${output} None



Connect DB
Connect To Database  pymysql  ${DBName}  ${DBUser}  ${DBPassword}  ${DBHost}  ${DBPort}