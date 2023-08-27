import base64
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "03748118C7003434",
    "appium:app": "D:\\.IT\\apk\\app-develop-debug.apk",
    "appium:automationName": "uiautomator2",
    "appium:caps[\"uiautomator2ServerInstallTimeout\"]": 60000
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
driver.implicitly_wait(30)

# start video record
driver.start_recording_screen()

# close wellcome screen
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view'
                              '.View/android.view.View[4]/android.view.View').click()

# skip for now
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view'
                              '.View/android.view.View[2]/android.widget.TextView').click()

# got it on the chat tooltip
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view'
                              '.View/android.view.View/android.widget.TextView').click()

# tap on search, enter keys
search_field = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose'
                              '.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android'
                              '.view.View[3]/android.widget.TextView')
search_field.click()
search_field_new = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                 '.widget.FrameLayout/androidx.compose.ui.platform.ComposeView'
                                                 '/android.view.View/android.view.View/android.view.View/android'
                                                 '.widget.EditText')
search_field_new.send_keys('car')

# script to tap on done
driver.execute_script('mobile:performEditorAction', {'action': 'done'})
# or we can hide keyboard
# driver.hide_keyboard()

# tap on Carry1st element
driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.compose'
                              '.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View/android'
                              '.view.View[4]/android.view.View/android.widget.TextView').click()

# scroll down, also we can tap, long press etc with TouchActions. We can enter coordinates or element created with Xpath previously

touch = TouchAction(driver)
time.sleep(8)
for i in range(2):
    touch.press(x=244, y=700)
    touch.move_to(x=244, y=100)
    touch.release().perform()

# make a screenshot
filename = time.strftime("%Y_%m_%d__%H_%M_%S") + driver.current_activity
driver.save_screenshot("D:\\.IT\\PythonQaTests\\Screenshots\\" + filename + ".png")



# stop video record
video_rawdata = driver.stop_recording_screen()
video_filename = time.strftime("%Y_%m_%d__%H_%M_%S") + driver.current_activity
with open("D:\\.IT\\PythonQaTests\\Screenshots\\" + video_filename + ".mp4", "wb") as final_video:
    final_video.write(base64.b64decode(video_rawdata))

