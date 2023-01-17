from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#Проверяем зачение атрибута "required" у "I'm the robot".
    people_radio = browser.find_element_by_id("robotCheckbox")
    the_robot = people_radio.get_attribute("required")
    print("velue of I'm the robot:", the_robot)
    assert the_robot is not None, "the_robot is not selected by default"

#Проверяем значение атрибута "checked" у "People rule".
    people_checked = browser.find_element_by_id("peopleRule")
    people_rule = people_checked.get_attribute("checked")
    print("velue of People rule:", people_rule)
    assert people_rule is not None, "people_rule is not selected by default"

#Проверяем значение "checked" у "Robots rule".
    robot_checked = browser.find_element_by_id("robotsRule")
    robot_rule = robot_checked.get_attribute("checked")
    print("velue of Robot rule:", robot_rule)
    assert robot_rule is None, "robot_rule is not selected by default"

#Проверяем значение "disabled" у "Submit".
    submit_checked = browser.find_element_by_css_selector(".btn.btn-default")
    submit_disabled = submit_checked.get_attribute("disabled")
    print("velue of button Submit:", submit_disabled)
    assert submit_disabled is None

#Проверяем значение "disabled" у "Submit" спустя - 10 секунд.
    time.sleep(10)
    submit_disabled = submit_checked.get_attribute("disabled")
    print("velue of button Submit after TEN seconds:", submit_disabled)
    assert submit_disabled is not None

finally:
    time.sleep(1)
    browser.quit()