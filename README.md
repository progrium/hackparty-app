# HackParty App

This is the application code for hackparty.org which manages user
accounts and the clone protocol for events.

## Contributors

* Jeff Lindsay <progrium@gmail.com>
* Ben McGraw <ben.mcgraw@gmail.com>
* Joël Franusic <joel@franusic.com>

## License

MIT

## Goals

* Scan QR code, get taken to a "pre-registration" page: "Put in your email"
* App sends an email with a URL
* URL directs to a "complete registration page"
* User gets created

## How to use:

This software is written for Google App Engine and is based on the Google App Engine SDK for Python.

Download the Google App Engine SDK for Python here: https://developers.google.com/appengine/downloads

There are two ways to run this software in a development environment:

1. Using the GoogleAppEngineLauncher 
2. Using the dev_appserver.py command

GoogleAppEngineLauncher:

* Install the Google App Engine SDK for Python
* Open the GoogleAppEngineLauncher
* File > New Application
* Name the application and navigate to where you've downloaded this code

dev_appserver.py:

* Install the Google App Engine SDK for Python
* Open the GoogleAppEngineLauncher
* GoogleAppEngineLauncher > Make Symlinks > Click "OK"
* Open a terminal
* "cd" to where you've downloaded this code
* Run "dev_appserver.py ."

