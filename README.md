SpriteCould Assignement

To who it may concern!

Thank you Sprite Cloud for the opportunity to step out of my familiar and comfortable area of expertise, in order to persue something a bit more technical and stimulating. 

When reviewing the scripts, I would like to note that, all the efforts placed into completing this assignment was entirely new territory for me. I have set up Selenium before on Windows Visual Studio using Java, however my reach regarding a script was as basic as it gets. Open google, do a search, open a web page.

Although I know what I am submitting is very basic, I am delighted to have made it this far and I'm nothing but grateful for the consideration.

With that said...

7a) How to Run the Tests Locally

-You will need PyCharm installed
-Navigate to https://github.com/Nash-ZA/SCAssignment.git and download this repository.
-Using PyCharm, open any of the tests in the Tests folder you just downloaded
-Ensure that these packages are installed on your project:
	>Selenium
	>pytest
-Place the chromedriver.exe (Found in Tests Folder) in: C:\Drivers\ChromeDriver\chromedriver.exe
-Place the img.jpg file (Found in Tests Folder) in: C:\Selenium\img.jpg     (Should you not want to use my amazing img file, you can use any other as long as it's in this directory)
-Execute the script by right clicking in the script window and clicking Run.
-If you wish to see the gui while executing, remove the "options=options" line when invoking the webdriver.

7b) In order to run the scripts using a CI/CD pipeline, I used Jenkins. After installing it on my local machine, I connected via localhost.
 -In Jenkins navigate to Your Dashboard and Select New Item
 -Give this Item a Name and select "Freestyle project"
 -Click on Ok
 -On the general tab, under Source Code Management, select Git
 -Specify the following Repository: https://github.com/Nash-ZA/SCAssignment.git
 -Specify your credentials by adding / selecting existing
 -Scroll down to build and add a build step "Custom Python Builder" (Do take note that you will need the ShiningPanda Plugin installed on your Jenkins environment to see Custom Python Builder")
 - Under the Home field, specify your python exe path
 - Nature leave as shell
 - For command, paste the following:

python -m venv env
call ./env/Scripts/activate.bat
pip install -r requirements.txt
pip install numpy pytest
pytest --junit-xml=TestReports/Web_DragAndDrop.xml ./Tests/Web_DragAndDrop.py
pytest --junit-xml=TestReports/Web_FormSubmissiont.xml ./Tests/Web_FormSubmission.py
pytest --junit-xml=TestReports/Web_Tables.xml ./Tests/Web_Tables.py

 -Execution should complete successfully

7c) I did upload the results to Calliope.pro but... haha, I still need to learn how to effectively mark the tests for JUnit to generate proper XML reports. Thats on my to-do list to learn going forward. I love how Calliope reads the report and would enjoy to see how it effectively reads a proper report.

https://app.calliope.pro/reports/110003
https://app.calliope.pro/reports/110004
https://app.calliope.pro/reports/110005

7d) My approach to identifying scenarios was purely based off of what would give me the most substance to learn in a short amount of time. Not only that, but I also wanted to look at areas where Worksoft can't tread at the moment. That being, drag and drop. From Submissions had a good all around use case with the multiple different objects with various action steps required to interact properly. Tables on the other hand, I was always curious how to use code to interact with it. So from a business requirement stand-point, I  didn't think about what would be critical focus areas for the business in this case. This was more of a opportunity to learn, as well as show my capability to learn and adapt as rapidly as possible.

Regarding API's, I tried my best to establish the fundamentals, as I have never done API testing before, let alone with Selenium / Python. The fundamentals are simple enough to grasp, however I really got stuck on the API_Keys and authenitcaiton Headers... It was also quite challanging to source some simple lesson or demonstration. I figure I would need to sit with someone to understand the basics of the execution. You will notice there are no scripts to review here as I don't have any. Every script I made failed and was very basic get and post methods to load and read users off the petstore database. When doing it on the page it worked fine. When running the scripts however, it failed and I need assistance to understand. Not sure if I was missing Curl commands or what the issue was.

7e) 
The reason I picked the scenarios for Web:
Drag and Drop -> this is functionality that is currently impossible with Worksoft Certify, so to me, this was an enterily new interaction which I enjoyed learning.
Form Submission -> this simple interface touched on various different interactions, radio buttons, autocomplete forms, upload bottons, text areas/fields. I felt like this is a wonderful all-round scenario to get an understanding of how most use cases would have to be approached for front end test execution.
Tables -> tables can typically be a challenge to interact with, and doing so with Selenium and Python was rather exciting. I feel there is a lot for me to learn

7f) The next steps for my project would be to LEARN!
	1. Learn how to effectively generate XML reports using JUnit
	2. Learn how to use a CI platform to execute API tests and get an understanding of Authorization, Headers and API testbeds
	3. Learn and Practice Keyword/Data Driven Framework with Selenium Python
	4. Familiarize myself further with Jenkins and GitHub.
	5. PRACTICE
