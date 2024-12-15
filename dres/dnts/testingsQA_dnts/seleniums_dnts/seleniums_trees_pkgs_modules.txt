seleniums_trees : pkgs / modules / class-tree / ...
=============================================================

#####  ==========  pkgs-selenium / dir-tree:
	_______:  pkgs: ----------------------------------------------
	[u1@2209arx site-packages]$ tree  selenium  -d
	selenium
	├── common
	└── webdriver
		├── chrome
		├── chromium
		├── common
		│   ├── actions
		│   ├── bidi
		│   ├── devtools ...
		│   ├── html5
		│   ├── linux
		│   ├── macos
		│   └── windows
		├── edge
		├── firefox
		├── ie
		├── remote
		├── safari
		├── support
		├── webkitgtk
		└── wpewebkit
##________________________________________  ___________________________


#####  ==========  modules /*.py-files

	_______:  modules:  -------------------------------------------
	- tree -P "*.py"   -I "__pyca*|devtools|*.js"   /home/u1/.local/lib/python3.10/site-packages/selenium
	/home/u1/.local/lib/python3.10/site-packages/selenium
	├── common
	│   ├── exceptions.py
	│   └── __init__.py
	├── __init__.py
	├── types.py
	└── webdriver
		├── chrome
		│   ├── __init__.py
		│   ├── options.py
		│   ├── service.py
		│   └── webdriver.py
		├── chromium
		│   ├── __init__.py
		│   ├── options.py
		│   ├── remote_connection.py
		│   ├── service.py
		│   └── webdriver.py
		├── common
		│   ├── action_chains.py
		│   ├── actions
		│   │   ├── action_builder.py
		│   │   ├── __init__.py
		│   │   ├── input_device.py
		│   │   ├── interaction.py
		│   │   ├── key_actions.py
		│   │   ├── key_input.py
		│   │   ├── mouse_button.py
		│   │   ├── pointer_actions.py
		│   │   ├── pointer_input.py
		│   │   ├── wheel_actions.py
		│   │   └── wheel_input.py
		│   ├── alert.py
		│   ├── bidi
		│   │   ├── cdp.py
		│   │   ├── console.py
		│   │   └── __init__.py
		│   ├── by.py
		│   ├── desired_capabilities.py
		│   ├── html5
		│   │   ├── application_cache.py
		│   │   └── __init__.py
		│   ├── __init__.py
		│   ├── keys.py
		│   ├── linux
		│   ├── log.py
		│   ├── macos
		│   ├── options.py
		│   ├── print_page_options.py
		│   ├── proxy.py
		│   ├── selenium_manager.py
		│   ├── service.py
		│   ├── timeouts.py
		│   ├── utils.py
		│   ├── virtual_authenticator.py
		│   ├── window.py
		│   └── windows
		├── edge
		│   ├── __init__.py
		│   ├── options.py
		│   ├── service.py
		│   └── webdriver.py
		├── firefox
		│   ├── extension_connection.py
		│   ├── firefox_binary.py
		│   ├── firefox_profile.py
		│   ├── __init__.py
		│   ├── options.py
		│   ├── remote_connection.py
		│   ├── service.py
		│   └── webdriver.py
		├── ie
		│   ├── __init__.py
		│   ├── options.py
		│   ├── service.py
		│   └── webdriver.py
		├── __init__.py
		├── remote
		│   ├── bidi_connection.py
		│   ├── command.py
		│   ├── errorhandler.py
		│   ├── file_detector.py
		│   ├── __init__.py
		│   ├── mobile.py
		│   ├── remote_connection.py
		│   ├── script_key.py
		│   ├── shadowroot.py
		│   ├── switch_to.py
		│   ├── utils.py
		│   ├── webdriver.py
		│   └── webelement.py
		├── safari
		│   ├── __init__.py
		│   ├── options.py
		│   ├── permissions.py
		│   ├── remote_connection.py
		│   ├── service.py
		│   └── webdriver.py
		├── support
		│   ├── abstract_event_listener.py
		│   ├── color.py
		│   ├── event_firing_webdriver.py
		│   ├── events.py
		│   ├── expected_conditions.py
		│   ├── __init__.py
		│   ├── relative_locator.py
		│   ├── select.py
		│   ├── ui.py
		│   └── wait.py
		├── webkitgtk
		│   ├── __init__.py
		│   ├── options.py
		│   ├── service.py
		│   └── webdriver.py
		└── wpewebkit
			├── __init__.py
			├── options.py
			├── service.py
			└── webdriver.py
	20 directories, 99 files
##________________________________________  ___________________________


#####  ==========  classes-names-listing--with-grep :

	_______  :		  classes-names-listing--with-grep: -------------------
	/home/u1/.local/lib/python3.10/site-packages
	[u1@2209arx site-packages]$ grep1  --include="*.py"   --exclude-dir="*devtool*"  -E "^class    " -R    ./selenium/  | sort
	./selenium/common/exceptions.py  :		class    ElementClickInterceptedException(WebDriverException):
	./selenium/common/exceptions.py  :		class    ElementNotInteractableException(InvalidElementStateException):
	./selenium/common/exceptions.py  :		class    ElementNotSelectableException(InvalidElementStateException):
	./selenium/common/exceptions.py  :		class    ElementNotVisibleException(InvalidElementStateException):
	./selenium/common/exceptions.py  :		class    ImeActivationFailedException(WebDriverException):
	./selenium/common/exceptions.py  :		class    ImeNotAvailableException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InsecureCertificateException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidArgumentException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidCookieDomainException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidCoordinatesException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidElementStateException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidSelectorException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidSessionIdException(WebDriverException):
	./selenium/common/exceptions.py  :		class    InvalidSwitchToTargetException(WebDriverException):
	./selenium/common/exceptions.py  :		class    JavascriptException(WebDriverException):
	./selenium/common/exceptions.py  :		class    MoveTargetOutOfBoundsException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoAlertPresentException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoSuchAttributeException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoSuchCookieException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoSuchElementException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoSuchFrameException(InvalidSwitchToTargetException):
	./selenium/common/exceptions.py  :		class    NoSuchShadowRootException(WebDriverException):
	./selenium/common/exceptions.py  :		class    NoSuchWindowException(InvalidSwitchToTargetException):
	./selenium/common/exceptions.py  :		class    ScreenshotException(WebDriverException):
	./selenium/common/exceptions.py  :		class    SeleniumManagerException(WebDriverException):
	./selenium/common/exceptions.py  :		class    SessionNotCreatedException(WebDriverException):
	./selenium/common/exceptions.py  :		class    StaleElementReferenceException(WebDriverException):
	./selenium/common/exceptions.py  :		class    TimeoutException(WebDriverException):
	./selenium/common/exceptions.py  :		class    UnableToSetCookieException(WebDriverException):
	./selenium/common/exceptions.py  :		class    UnexpectedAlertPresentException(WebDriverException):
	./selenium/common/exceptions.py  :		class    UnexpectedTagNameException(WebDriverException):
	./selenium/common/exceptions.py  :		class    UnknownMethodException(WebDriverException):
	./selenium/common/exceptions.py  :		class    WebDriverException(Exception):
	./selenium/webdriver/chrome/options.py  :		class    Options(ChromiumOptions):
	./selenium/webdriver/chrome/service.py  :		class    Service(service.ChromiumService):
	./selenium/webdriver/chrome/webdriver.py  :		class    WebDriver(ChromiumDriver):
	./selenium/webdriver/chromium/options.py  :		class    ChromiumOptions(ArgOptions):
	./selenium/webdriver/chromium/remote_connection.py  :		class    ChromiumRemoteConnection(RemoteConnection):
	./selenium/webdriver/chromium/service.py  :		class    ChromiumService(service.Service):
	./selenium/webdriver/chromium/webdriver.py  :		class    ChromiumDriver(RemoteWebDriver):
	./selenium/webdriver/common/action_chains.py  :		class    ActionChains:
	./selenium/webdriver/common/actions/action_builder.py  :		class    ActionBuilder:
	./selenium/webdriver/common/actions/input_device.py  :		class    InputDevice:
	./selenium/webdriver/common/actions/interaction.py  :		class    Interaction:
	./selenium/webdriver/common/actions/interaction.py  :		class    Pause(Interaction):
	./selenium/webdriver/common/actions/key_actions.py  :		class    KeyActions(Interaction):
	./selenium/webdriver/common/actions/key_input.py  :		class    KeyInput(InputDevice):
	./selenium/webdriver/common/actions/key_input.py  :		class    TypingInteraction(Interaction):
	./selenium/webdriver/common/actions/mouse_button.py  :		class    MouseButton:
	./selenium/webdriver/common/actions/pointer_actions.py  :		class    PointerActions(Interaction):
	./selenium/webdriver/common/actions/pointer_input.py  :		class    PointerInput(InputDevice):
	./selenium/webdriver/common/actions/wheel_actions.py  :		class    WheelActions(Interaction):
	./selenium/webdriver/common/actions/wheel_input.py  :		class    ScrollOrigin:
	./selenium/webdriver/common/actions/wheel_input.py  :		class    WheelInput(InputDevice):
	./selenium/webdriver/common/alert.py  :		class    Alert:
	./selenium/webdriver/common/bidi/cdp.py  :		class    BrowserError(Exception):
	./selenium/webdriver/common/bidi/cdp.py  :		class    CdpBase:
	./selenium/webdriver/common/bidi/cdp.py  :		class    CdpConnection(CdpBase, trio.abc.AsyncResource):
	./selenium/webdriver/common/bidi/cdp.py  :		class    CdpConnectionClosed(WsConnectionClosed):
	./selenium/webdriver/common/bidi/cdp.py  :		class    CdpSession(CdpBase):
	./selenium/webdriver/common/bidi/cdp.py  :		class    CmEventProxy:
	./selenium/webdriver/common/bidi/cdp.py  :		class    InternalError(Exception):
	./selenium/webdriver/common/bidi/console.py  :		class    Console(Enum):
	./selenium/webdriver/common/by.py  :		class    By:
	./selenium/webdriver/common/desired_capabilities.py  :		class    DesiredCapabilities:
	./selenium/webdriver/common/html5/application_cache.py  :		class    ApplicationCache:
	./selenium/webdriver/common/keys.py  :		class    Keys:
	./selenium/webdriver/common/log.py  :		class    Log:
	./selenium/webdriver/common/options.py  :		class    ArgOptions(BaseOptions):
	./selenium/webdriver/common/options.py  :		class    BaseOptions(metaclass=ABCMeta):
	./selenium/webdriver/common/print_page_options.py  :		class    PrintOptions:
	./selenium/webdriver/common/proxy.py  :		class    Proxy:
	./selenium/webdriver/common/proxy.py  :		class    ProxyType:
	./selenium/webdriver/common/proxy.py  :		class    ProxyTypeFactory:
	./selenium/webdriver/common/selenium_manager.py  :		class    SeleniumManager:
	./selenium/webdriver/common/service.py  :		class    Service(ABC):
	./selenium/webdriver/common/timeouts.py  :		class    Timeouts:
	./selenium/webdriver/common/virtual_authenticator.py  :		class    Credential:
	./selenium/webdriver/common/virtual_authenticator.py  :		class    Protocol(str, Enum):
	./selenium/webdriver/common/virtual_authenticator.py  :		class    Transport(str, Enum):
	./selenium/webdriver/common/virtual_authenticator.py  :		class    VirtualAuthenticatorOptions:
	./selenium/webdriver/common/window.py  :		class    WindowTypes:
	./selenium/webdriver/edge/options.py  :		class    Options(ChromiumOptions):
	./selenium/webdriver/edge/service.py  :		class    Service(service.ChromiumService):
	./selenium/webdriver/edge/webdriver.py  :		class    WebDriver(ChromiumDriver):
	./selenium/webdriver/firefox/extension_connection.py  :		class    ExtensionConnectionError(Exception):
	./selenium/webdriver/firefox/extension_connection.py  :		class    ExtensionConnection(RemoteConnection):
	./selenium/webdriver/firefox/firefox_binary.py  :		class    FirefoxBinary:
	./selenium/webdriver/firefox/firefox_profile.py  :		class    AddonFormatError(Exception):
	./selenium/webdriver/firefox/firefox_profile.py  :		class    FirefoxProfile:
	./selenium/webdriver/firefox/options.py  :		class    Log:
	./selenium/webdriver/firefox/options.py  :		class    Options(ArgOptions):
	./selenium/webdriver/firefox/remote_connection.py  :		class    FirefoxRemoteConnection(RemoteConnection):
	./selenium/webdriver/firefox/service.py  :		class    Service(service.Service):
	./selenium/webdriver/firefox/webdriver.py  :		class    WebDriver(RemoteWebDriver):
	./selenium/webdriver/ie/options.py  :		class    ElementScrollBehavior(Enum):
	./selenium/webdriver/ie/options.py  :		class    Options(ArgOptions):
	./selenium/webdriver/ie/service.py  :		class    Service(service.Service):
	./selenium/webdriver/ie/webdriver.py  :		class    WebDriver(RemoteWebDriver):
	./selenium/webdriver/remote/bidi_connection.py  :		class    BidiConnection:
	./selenium/webdriver/remote/command.py  :		class    Command:
	./selenium/webdriver/remote/errorhandler.py  :		class    ErrorCode:
	./selenium/webdriver/remote/errorhandler.py  :		class    ErrorHandler:
	./selenium/webdriver/remote/file_detector.py  :		class    FileDetector(metaclass=ABCMeta):
	./selenium/webdriver/remote/file_detector.py  :		class    LocalFileDetector(FileDetector):
	./selenium/webdriver/remote/file_detector.py  :		class    UselessFileDetector(FileDetector):
	./selenium/webdriver/remote/mobile.py  :		class    Mobile:
	./selenium/webdriver/remote/remote_connection.py  :		class    RemoteConnection:
	./selenium/webdriver/remote/script_key.py  :		class    ScriptKey:
	./selenium/webdriver/remote/shadowroot.py  :		class    ShadowRoot:
	./selenium/webdriver/remote/switch_to.py  :		class    SwitchTo:
	./selenium/webdriver/remote/webdriver.py  :		class    BaseWebDriver(metaclass=ABCMeta):
	./selenium/webdriver/remote/webdriver.py  :		class    WebDriver(BaseWebDriver):
	./selenium/webdriver/remote/webelement.py  :		class    BaseWebElement(metaclass=ABCMeta):
	./selenium/webdriver/remote/webelement.py  :		class    WebElement(BaseWebElement):
	./selenium/webdriver/safari/options.py  :		class    Log:
	./selenium/webdriver/safari/options.py  :		class    Options(ArgOptions):
	./selenium/webdriver/safari/permissions.py  :		class    Permission:
	./selenium/webdriver/safari/remote_connection.py  :		class    SafariRemoteConnection(RemoteConnection):
	./selenium/webdriver/safari/service.py  :		class    Service(service.Service):
	./selenium/webdriver/safari/webdriver.py  :		class    WebDriver(RemoteWebDriver):
	./selenium/webdriver/support/abstract_event_listener.py  :		class    AbstractEventListener:
	./selenium/webdriver/support/color.py  :		class    Color:
	./selenium/webdriver/support/event_firing_webdriver.py  :		class    EventFiringWebDriver:
	./selenium/webdriver/support/event_firing_webdriver.py  :		class    EventFiringWebElement:
	./selenium/webdriver/support/relative_locator.py  :		class    RelativeBy:
	./selenium/webdriver/support/select.py  :		class    Select:
	./selenium/webdriver/support/wait.py  :		class    WebDriverWait:
	./selenium/webdriver/webkitgtk/options.py  :		class    Options(ArgOptions):
	./selenium/webdriver/webkitgtk/service.py  :		class    Service(service.Service):
	./selenium/webdriver/webkitgtk/webdriver.py  :		class    WebDriver(RemoteWebDriver):
	./selenium/webdriver/wpewebkit/options.py  :		class    Options(ArgOptions):
	./selenium/webdriver/wpewebkit/service.py  :		class    Service(service.Service):
	./selenium/webdriver/wpewebkit/webdriver.py  :		class    WebDriver(RemoteWebDriver):
	[u1@2209arx site-packages]$ 
##________________________________________  ___________________________


#####  ==========  classesTree-4-levels:

    ---------- selenium.webdriver.remote.webdriver.BaseWebDriver : ----------
    -|  BaseWebDriver  	 : <class 'selenium.webdriver.remote.webdriver.BaseWebDriver'>
    -| -|  WebDriver  	 : <class 'selenium.webdriver.remote.webdriver.WebDriver'>
    -| -| -|  ChromiumDriver  	 : <class 'selenium.webdriver.chromium.webdriver.ChromiumDriver'>
    -| -| -| -|  WebDriver  	 : <class 'selenium.webdriver.chrome.webdriver.WebDriver'>
    -| -| -| -|  WebDriver  	 : <class 'selenium.webdriver.edge.webdriver.WebDriver'>
    -| -| -|  WebDriver  	 : <class 'selenium.webdriver.firefox.webdriver.WebDriver'>
    -| -| -|  WebDriver  	 : <class 'selenium.webdriver.ie.webdriver.WebDriver'>
    -| -| -|  WebDriver  	 : <class 'selenium.webdriver.safari.webdriver.WebDriver'>
    -| -| -|  WebDriver  	 : <class 'selenium.webdriver.webkitgtk.webdriver.WebDriver'>
    -| -| -|  WebDriver  	 : <class 'selenium.webdriver.wpewebkit.webdriver.WebDriver'>
    -----------------------------

    ---------- selenium.common.exceptions.WebDriverException : ----------
    -|  WebDriverException  	 : <class 'selenium.common.exceptions.WebDriverException'>
    -| -|  InvalidSwitchToTargetException  	 : <class 'selenium.common.exceptions.InvalidSwitchToTargetException'>
    -| -| -|  NoSuchFrameException  	 : <class 'selenium.common.exceptions.NoSuchFrameException'>
    -| -| -|  NoSuchWindowException  	 : <class 'selenium.common.exceptions.NoSuchWindowException'>
    -| -|  NoSuchElementException  	 : <class 'selenium.common.exceptions.NoSuchElementException'>
    -| -|  NoSuchAttributeException  	 : <class 'selenium.common.exceptions.NoSuchAttributeException'>
    -| -|  NoSuchShadowRootException  	 : <class 'selenium.common.exceptions.NoSuchShadowRootException'>
    -| -|  StaleElementReferenceException  	 : <class 'selenium.common.exceptions.StaleElementReferenceException'>
    -| -|  InvalidElementStateException  	 : <class 'selenium.common.exceptions.InvalidElementStateException'>
    -| -| -|  ElementNotVisibleException  	 : <class 'selenium.common.exceptions.ElementNotVisibleException'>
    -| -| -|  ElementNotInteractableException  	 : <class 'selenium.common.exceptions.ElementNotInteractableException'>
    -| -| -|  ElementNotSelectableException  	 : <class 'selenium.common.exceptions.ElementNotSelectableException'>
    -| -|  UnexpectedAlertPresentException  	 : <class 'selenium.common.exceptions.UnexpectedAlertPresentException'>
    -| -|  NoAlertPresentException  	 : <class 'selenium.common.exceptions.NoAlertPresentException'>
    -| -|  InvalidCookieDomainException  	 : <class 'selenium.common.exceptions.InvalidCookieDomainException'>
    -| -|  UnableToSetCookieException  	 : <class 'selenium.common.exceptions.UnableToSetCookieException'>
    -| -|  TimeoutException  	 : <class 'selenium.common.exceptions.TimeoutException'>
    -| -|  MoveTargetOutOfBoundsException  	 : <class 'selenium.common.exceptions.MoveTargetOutOfBoundsException'>
    -| -|  UnexpectedTagNameException  	 : <class 'selenium.common.exceptions.UnexpectedTagNameException'>
    -| -|  InvalidSelectorException  	 : <class 'selenium.common.exceptions.InvalidSelectorException'>
    -| -|  ImeNotAvailableException  	 : <class 'selenium.common.exceptions.ImeNotAvailableException'>
    -| -|  ImeActivationFailedException  	 : <class 'selenium.common.exceptions.ImeActivationFailedException'>
    -| -|  InvalidArgumentException  	 : <class 'selenium.common.exceptions.InvalidArgumentException'>
    -| -|  JavascriptException  	 : <class 'selenium.common.exceptions.JavascriptException'>
    -| -|  NoSuchCookieException  	 : <class 'selenium.common.exceptions.NoSuchCookieException'>
    -| -|  ScreenshotException  	 : <class 'selenium.common.exceptions.ScreenshotException'>
    -| -|  ElementClickInterceptedException  	 : <class 'selenium.common.exceptions.ElementClickInterceptedException'>
    -| -|  InsecureCertificateException  	 : <class 'selenium.common.exceptions.InsecureCertificateException'>
    -| -|  InvalidCoordinatesException  	 : <class 'selenium.common.exceptions.InvalidCoordinatesException'>
    -| -|  InvalidSessionIdException  	 : <class 'selenium.common.exceptions.InvalidSessionIdException'>
    -| -|  SessionNotCreatedException  	 : <class 'selenium.common.exceptions.SessionNotCreatedException'>
    -| -|  UnknownMethodException  	 : <class 'selenium.common.exceptions.UnknownMethodException'>
    -| -|  SeleniumManagerException  	 : <class 'selenium.common.exceptions.SeleniumManagerException'>
##________________________________________  ___________________________

