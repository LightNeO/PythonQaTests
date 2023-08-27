from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "03748118C7003434",
    "appium:app": "D:\\.IT\\apk\\app-develop-debug.apk",
    "appium:automationName": "uiautomator2",
    "appium:caps[\"uiautomator2ServerInstallTimeout\"]": 60000
}

driver =  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
