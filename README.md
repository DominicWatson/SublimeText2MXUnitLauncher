MXUnit Test Launcher Plugin for Sublime Text 2
----------------------------------------------

Provides commands for launching the currently open file as an MXUnit test case (opens in browser) and for launching an MXUnit testsuite.

Settings
--------

You can get to the settings through Preferences->Package Settings->MXUnit. Options are:

* **base_url**: The root url for your tests, *without* trailing slash. e.g. http://localhost/tests
* **base_path**: The root path on your machine that maps to the url, *without* trailing slash
* **test_suite**: Url, relative to the base_url, for running a test suite, e.g. /TestSuite.cfm

Example Settings Configuration
------------------------------

```JavaScript
{
    "base_url":"http://localhost",
    "base_path":"C:\\webroot\\webapp",
    "test_suite":"/webapp/test/TestSuite.cfm"
}
```

Commands
--------

* **launch_test**: Launches the current file as an MXUnit test in the browser (shift-alt-t)
* **launch_test_suite**: Launches the test suite in the browser (shift-alt-s)

Windows Installation (XP, Vista & Windows 7)
--------------------------------------------
* Download and Unzip package from the GitHub project page
* Create a folder in %AppData%\Sublime Text 2\Packages called "MxUnit"
* Copy the contents of the unzipped folder to %AppData%\Sublime Text 2\Packages\MxUnit
* Restart Sublime Text 2