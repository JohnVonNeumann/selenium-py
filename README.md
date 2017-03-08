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
