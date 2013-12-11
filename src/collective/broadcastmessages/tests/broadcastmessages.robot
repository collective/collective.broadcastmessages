*** Settings ***
Resource  plone/app/robotframework/variables.robot
Library  Selenium2Library  timeout=10  implicit_wait=0.5
Library  Remote  ${PLONE_URL}/RobotRemote
Library  plone.app.robotframework.keywords.Debugging

Suite Setup  Start browser
Suite Teardown  Close All Browsers

*** Variables ***

${BROWSER} =  firefox

*** Test Cases ***

Anonymous may not view broadcast messages
    Go to  http://localhost:55001/plone/
    Page should contain  Plone site
    Page should not contain element  css=div#broadcast-messages
    #Stop

When no message configured, authenticated view no broadcast messages
    [Tags]  start
    Enable autologin as  Authenticated
    Go to  http://localhost:55001/plone/
    Page should contain  Plone site
    Page should not contain element  css=div#broadcast-messages

*** Keywords ***

Start browser
    Open browser  http://localhost:55001/plone/  browser=${BROWSER}
