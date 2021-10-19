Feature:  Wowdare User Side End to End Functionality



  @home_page
  Scenario: To check the functionality of the Home_Page With Valid & Invalid Data.
  Given  User open Browser, Enter Url, Navigate To Log_in Page
  When   User Enter Username With Invalid Data
  And    Click On start Button
  And    User Enter Username With valid Data
  And    User Click on Start Button
  Then   User Should be Navigate to Question Page  Successfully



   @question_Page
  Scenario: Check the functionality of Question Page
  When   Click On Q1
  And    Validate onesignal pop-up functionality With click on Later Button
  And    Click On Q2
  And    Click On Q3
  And    Click On Q4
  And    Click On Q5
  And    Click On Q6
  And    Click On Q7
  And    Click On Q8
  And    Click On Q9
  And    Click On Q10
  And    Click On Q11
  And    Click On Q12
  And    Click On Q13
  And    Click On Q14

   @question_Page
  Scenario: To check the functionality of Question_Page Skip Button And  Navigate To Share Page
   Given  Validate Skip Button functionality
   When   Click On Q15
   Then   User Should be Navigate to Share Page  Successfully

    @share_page
   Scenario: To check the functionality of Share Page
   When   Click On Copy link_Button


 @Accept_Page
  Scenario: To Check the functionality of Accept_Page With Valid & Invalid Data.
  Given  User Friend open Browser, Enter Url, Navigate To Log_in Page

  When   User Friend Enter Username With Invalid Data
  And    User Friend Click On start Button
  And    User Friend Validate onesignal pop-up functionality With click on Later Button
  And    User Friend Enter Username With Valid Data
  And    User Friend Click on Start Buttons
  Then   User Friend Should be Navigate to Answer Page  Successfully

  @Answer_page
  Scenario: Check the functionality of Answer Page
  When   User Friend Click On Q1
  And    User Friend Click On Q2
  And    User Friend Click On Q3
  And    User Friend Click On Q4
  And    User Friend Click On Q5
  And    User Friend Click On Q6
  And    User Friend Click On Q7
  And    User Friend Click On Q8
  And    User Friend Click On Q9
  And    User Friend Click On Q10
  And    User Friend Click On Q11
  And    User Friend Click On Q12
  And    User Friend Click On Q13
  And    User Friend Click On Q14
  And    User Friend Click On Q15
  Then   User Friend Should be Navigate to Complete Page  Successfully

  @Complete_page
   Scenario: To check the functionality of Complete Page
   When   User Friend Click On Create Your Quiz Button
   Then   User Friend Become User And Navigate To Home Page


   @share_page
   Scenario: To check the functionality of Share Page Scoreboard and View Buttons
   Given  Validate the Scoreboard  Button Functionality
   When   User Click On View_Button
   Then   User Should Be Navigate To View Page

    @View_page
   Scenario: To check the functionality of View Page
   When   User Click On Back_Button And Should Be Navigate To Share Page
   And    Again User Click On View_Button And Navigate To View Page
   And    Click On View_page Delete Button
   Then   A Delete Pop_Up Should Be Open With Yes Or No Button Click On No Button
   Then   Click On Yes Button
   Then   Particular User Friend Entire Data Should Be Deleted And User Should Be Navigate To Share_page

   @share_page
   Scenario: To check the functionality of Share Page Delete Buttons
   When   Click On share_page Delete Button
   Then   A Delete Pop_Up Should Be Open And  Click On No Button
   Then   Click On Yes Button Share Page
   Then   Entire Quiz Should Be Deleted And User Navigate To The Home Page.


