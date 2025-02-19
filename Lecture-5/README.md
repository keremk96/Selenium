## Wait Commands

In Selenium, wait commands are used to synchronize the execution of test scripts with the state of the web application. Wait Commands help ensure that the script waits for certain conditions to be met before proceeding, which is crucial for dynamic web pages where elements may take time to load.

This helps in avoiding exceptions that occur when the elements to be tested are not loaded. Wait commands are essential when it comes to executing Selenium tests. They help to observe and troubleshoot issues that may occur due to variation in time lag.

While running Selenium tests, it is common for testers to get the message “Element Not Visible Exception“. This appears when a particular web element with which WebDriver has to interact, is delayed in its loading. To prevent this Exception, Selenium Wait Commands must be used.

## Implicit Wait

Implicit wait makes WebDriver to wait for a specified amount of time when trying to locate an element before throwing a NoSuchElementException. When implicit wait is set, the WebDriver will wait for a defined period, allowing for elements to load dynamically.

Implicit Wait setting is a Global setting and applies to all elements in the script, and it remains in effect for the duration of the WebDriver instance.

Once the command is run, Implicit Wait remains for the entire duration for which the browser is open. 

<img width="316" alt="Screenshot 2025-02-19 at 21 12 05" src="https://github.com/user-attachments/assets/c60f85df-46af-478b-a838-2d30ec5a20d5" />

## Explicit Wait

Explicit wait in Selenium is a synchronization mechanism that allows the WebDriver to wait for a specific condition to occur before proceeding with the next step in the code. Unlike Implicit waits, which apply globally, explicit waits are applied only to specific elements or conditions, making them more flexible and precise.

Setting Explicit Wait is important in cases where there are certain elements that naturally take more time to load. If one sets an implicit wait command, then the browser will wait for the same time frame before loading every web element. This causes an unnecessary delay in executing the test script.

<img width="802" alt="Screenshot 2025-02-19 at 21 27 12" src="https://github.com/user-attachments/assets/dcc01590-815e-464b-a6bf-22884f4bcd45" />

<img width="560" alt="Screenshot 2025-02-19 at 21 12 14" src="https://github.com/user-attachments/assets/3f62d473-0e2c-4087-8baa-4cde90146ac4" />

<img width="772" alt="Screenshot 2025-02-19 at 21 27 32" src="https://github.com/user-attachments/assets/1045d670-0106-4bea-a182-9d7d188d859d" />
