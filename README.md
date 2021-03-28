#Inspiration
During the pandemic, when schools shifted to an online environment, they had to deal with a unique predicament: conducting tests and exams. Most of the methods employed by schools like Google forms had a major flaw- students could easily cheat. Seeing our own college struggle to regulate tests, we decided to build a solution to this problem.

#What it does
Our project, SecuriTest, is an online portal where time-bound tests in the form of MCQs can be hosted. These tests are automatically graded. During the test, the questions are represented as images in order to discourage test-takers from copying the text. Moreover, the test to locked to the active tab, and if the browser tab is switched, the test is invalidated. Details about the test-taker like the Student ID and IP address are recorded in order to prevent multiple submissions. The website also displays a chart that depicts the performance of a student across all the tests.

#How we built it
We used the Python framework called Flask to build the backend and used HTML, CSS and JavaScript for the frontend. The backend uses a MySQL database. The website is hosted on PythonAnywhere.

#Challenges we ran into
We ran into a number of issues but we have done our best to overcome them all. One of them was to look for mechanisms to discourage malpractice. We also had to look for ways in which every student would be asked different questions and handle the situation where a student would want to resume an active test (therefore, the same questions that were presented earlier should be asked now).

#Accomplishments that we're proud of
We are very that we could accomplish our aim to make the test-taking process fairer. Features like restricting user responses without an authentication portal, preventing tab switches etc are the ones which we are proud of.

#What we learned
During the development of the project, we learned the process of developing websites using frameworks like Flask. We also learned how to handle simultaneous requests from multiple users, mechanisms to make the test-setting and test-taking processes as streamlined as possible.

#What's next for SecuriTest
Due to the time constraint during the hackathon, we, unfortunately, had to sacrifice a few additional features. Beyond the hackathon, we want to take this project forward by adding components like video and audio tracking among other add-ons.

#Try it out on:
[SecuriTest](http://www.securitest.pythonanywhere.com)
