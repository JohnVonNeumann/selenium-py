# selenium-py

Learning Selenium to help improve my test automation skills. Using Python instead of Java to improve Py skills whilst I'm at it.

> The best working example I have is the FindByIdName script. I am updating it with more and more advanced stuff as I go.

* Been spending some time getting Firepath setup for using xpath, strange how they bundle the thing into firefox but then they don't support some basic addon functionality. Had to go back to firebug vxx.18 in order to get the xpath stuff working. Even then, might have to port back further seeing as the course i'm only recommended much older than .18

* Now have webdrivers running for Chrome and Firefox, I'll build tests for those two. Anything more than that I can learn on the job when I come across them.

* Created my first gitignore file with this project, was containing log files that weren't required to be publicly viewable.

* After completing two different tutorials on finding by name, id, xpath and whatnot. I've decided that I have enough of a fundamental understanding and have decided to move on with what I'm working on. I'm now on logging of test results which is interesting. I have made the choice to continue on with more advanced topics as I need to get upto scratch on this topic quickly and not just continue with easy stuff. I won't improve at the rate I need to.

* Been doing some reading and install of the Selenium IDE, I'm trying to suss if it's better to use that over writing the tests. I would assume that it's probably better to write them yourself unless you were previously a manual tester who did point and click type stuff. For my purposes, I'll just stick to writing.

* Covered some logging stuff which is pretty interesting to be honest. I have realised that much of the course I'm doing is simply the guy going through the relevant doc sets and putting them in video format. Makes a lot of sense now how so many Udemy courses are built. Smart really. So the logging stuff is cool, I'm looking forward to further implementations where we are doing more dynamic stuff, ie: actually handling log data and relaying using the StreamHandler we setup.

* Making a lot of headway with this subject, getting some solid understanding of it now.

* Generating a better understanding of the role loggers and handlers play together. So with the logger, you can set it up to just save files in xx.log or if you have more realistic requirements (as in proper production), you'll use handlers. These handlers work at a setLevel, so you may set a streamHandler for stdout at a warning level, now all warning level logs will be sent out in the form of a stream to a predetermined destination. You may setLevel a fileHandler for debug, so ALL logs are logged to a local file. So you set a logger level at the start, then with the levels left inside that logger, ie: you set at debug, all levels of logging remian. You set logger at warning, you only have 2 levels up to set to handlers and work with.

* Finally got the logging stuff finished, was interesting to see how they work. Obviously I just grazed the surface and there would be a lot more depth to it, but it was cool seeing how they are put together and formatted and whatnot.

* Moved onto the more indepth assertion stuff, skipping a lot of basic content, adding a quick assert example just to get a simple example written down and whatnot. Pretty sure I understand the thing but yeah, quick one before I move onto implementing more complex stuff.

* So I'm now upto this section involving pyTest and I don't think this is still to do with Selenium so I'm probably gonna now go backwards in content and start doing more action and item specific stuff on selenium. Build out a test suite with them all. Mainly making this decision because I have been asked recently to get to grips with Selenium and at the risk of taking instructions too explicitly. It's probably better to stick with explicit Selenium than "kinda relates to selenium".

* So instead of fucking around with course videos, I'm just gonna go through each element of the site and write tests for it. I'll keep this suite together in the kode_it_test_suite.py file that I've just built. This will be my personal attempt at building an entire test suite to demonstrate my Selenium knowledge. At this stage I intend to keep it as one file. But as I go, I may decide that separating it into different files is more appropriate.

* Just had a bit of a lightbulb moment, so earlier when I was moving through the logging related parts, I was thinking that much of the log output is really quite skimpy, there isn't a whole lot of info. But just a second ago as I was adding tearDown methods to my new test suite I realised that as you write tests to succeed and fail, you would probably be adding calls to your log module and giving the relative failures and successes their own log messages, IE: If you work on a a test that revolves around something application breaking, you are going to give it a Critical tag perhaps, then add a relevant log output for recording in Stream and/or FileHanlders. So my thoughts on it being "not enough" I think were correct, I just didn't realise that the builder of tests is most likely the one adding messages to be displayed to log files in the event of those conditions being triggered.
