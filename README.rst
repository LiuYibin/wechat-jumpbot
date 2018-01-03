##############################################################################
Wechat Jump Bot (iOS)
##############################################################################

==============================================================================
Features
==============================================================================

- Auto Mode: playing the game automatically;
- Manual Mode: playing the game by manual.


==============================================================================
How it runs
==============================================================================

Prequsites

- WebDriverAgent
- libimobiledevice
- Python 3

WebDriverAgent

::

    $ git clone https://github.com/facebook/WebDriverAgent && cd WebDriverAgent
    $ brew install carthage
    $ ./Scripts/bootstrap.sh
    # open WebDriverAgent.xcodeproj with Xcode
    # Xcode:
    # - code sign (general and build_settings): WebDriverAgentLib/WebDriverAgentRunner
    # - Product -> Destination -> <your device>
    # - Product -> Scheme -> WebDriverAgentRunner
    # - Product -> Test

libimobiledevice (iproxy)

::

    $ brew install libimobiledevice
    $ iproxy 8100 8100
    # browse: http://localhost:8100/status
    # browse: http://localhost:8100/inspector

Bot Agent (iOS)

::

    $ git clone https://github.com/alpesis-ai/bot-agent-ios.git
    $ cd bot-agent-ios

    $ pip3 install --pre facebook-wda
    $ pip3 install -r requirements.txt
    $ make run

