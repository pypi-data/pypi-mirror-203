import time
import requests
from loguru import logger
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip

class MrFix:

    def assertElementsIsPresentByXpatch(self, xpath_elements):
        try:
            elements = self.find_elements(By.XPATH, xpath_elements)
            return [True, len(elements)]
        except NoSuchElementException:
            return [False, 0]

    def assertElementIsPresentByXPath_Click(self, xpath, msg=None):
        try:
            element = self.find_element(By.XPATH, xpath).click()
            return True
        except NoSuchElementException:
            return False

    def assertElementIsPresentByXPath_Send(self, xpath_input, send_message):
        try:
            element = self.find_element(By.XPATH, xpath_input)
            element.clear()
            length = len(element.get_attribute('value'))
            element.send_keys(length * Keys.BACKSPACE)
            time.sleep(2)
            element.send_keys(send_message)
            return True
        except NoSuchElementException:
            return (False)

    def check_exists_by_xpath(self, xpath):
        try:
            self.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True

    def select_and_click_element(self, xpath):
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath), f'Элемента {xpath} на странице нет'

    def select_and_send_in_input(self, xpath_input, send_message) -> object:
        assert MrFix.assertElementIsPresentByXPath_Send(self, xpath_input,
                                                           send_message), f'Элемента {xpath_input} на странице нет'

    def check_exists_elements_count(self, xpath_elements):
        elements_array = MrFix.assertElementsIsPresentByXpatch(self, xpath_elements)
        assert elements_array[0], f'Элементов {xpath_elements} на странице нет'
        return elements_array

    def scroll_down_and_click_element(self, xpath_down_link):

        SCROLL_PAUSE_TIME = 0.5
        # Get scroll height
        last_height = self.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            self.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        assert MrFix.assertElementIsPresentByXPath_Click(self,
                                                            xpath_down_link), f'Элемент {xpath_down_link} внизу страницы не обнаружен'

    def select_drop_down_element_text(self, xpath_drop_down_list, element_text):

        element = self.find_element(By.XPATH, xpath_drop_down_list)
        element.click()
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            if option.get_attribute("text") == element_text:  # print("Value is: %s" % option.get_attribute("value"))
                option.click()
                break

    def select_element_and_click_enter(self, xpath_element):
        self.find_element(By.XPATH, xpath_element).send_keys(Keys.RETURN)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath_element), f'Элемента {xpath_element} на странице нет'

    def autorization_user(self, url, login, password):
        session = requests.Session()
        session.post(url, {
            'username': login,
            'password': password,
            'remember': 1,
        })

    def uploading_file(self, xpath_input_file, file_path):
        self.find_element(By.XPATH, xpath_input_file).send_keys(file_path)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath_input_file), f'Элемента {xpath_input_file} на странице нет'

    def logging_file(log_file):
        logger.remove()
        logger.add(log_file, level='INFO',
                   format="<lvl>[</lvl><c>{time:DD.MM.YYYY HH:mm:ss.SSS}</c><lvl>]</lvl> <lvl>{message}</lvl>",
                   catch='True')

    def get_elements_array(self, xpath_elements):
        elements_array = self.find_elements(By.XPATH, xpath_elements)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath_elements), f'Элемента {xpath_elements} на странице нет'
        return elements_array


    def switch_to_current_window(self):
        self.switch_to.active_element
        handles = self.window_handles
        for handle in handles:
            if self.current_window_handle != handle:
                # Закрываем первое окно
                self.close()
                # переключаемся на второе окно', handle
                self.switch_to.window(handle)

    def get_elements_attribute(self, xpath_element, attribute):
        element = self.find_element(By.XPATH, xpath_element)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath_element), f'Элемента {xpath_element} на странице нет'
        return element.get_attribute(attribute)

    def get_text_of_element(self, xpath_element):
        element = self.find_element(By.XPATH, xpath_element)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath_element), f'Элемента {xpath_element} на странице нет'
        return element.text

    def clear_input_element(self, xpath_element):
        element = self.find_element(By.XPATH, xpath_element)
        element.clear()
        length = len(element.get_attribute('value'))
        element.send_keys(length * Keys.BACKSPACE)

    def press_down_arrow_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.ARROW_DOWN)
            time.sleep(.1)
        action.perform()

    def press_up_arrow_key_up(self, n):
        action = ActionChains(self)
        for i in range(n):
            action.send_keys(Keys.ARROW_UP)
            time.sleep(0.1)

    def press_enter_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.RETURN)
            time.sleep(.1)
        action.perform()

    def press_tab_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.TAB)
            time.sleep(.1)
        action.perform()

    def press_backspace_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.BACKSPACE)
            time.sleep(.1)
        action.perform()

    def press_space_key(self, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(Keys.SPACE)
            time.sleep(.1)
        action.perform()

    def press_char(self, char, n):
        action = ActionChains(self)
        for _ in range(n):
            action.send_keys(char)
            time.sleep(.1)
        action.perform()

    def find_and_click_text_link(self, text):
        try:
            self.find_element_by_partial_link_text(text).click()
            return True
        except NoSuchElementException:
            return False

    def find_and_return_href_on_page(self, link):
        link_exists = False
        url = ''
        elems = self.find_element(By.XPATH, "//a[@href]")
        for elem in elems:
            s = elem.get_attribute("href")
            if link in s:
                link_exists = True
                url = s
        m = []
        m.append(link_exists)
        m.append(url)
        return m

    def check_url(url):
        try:
            url_exists = True
            response = requests.get(url)
        except ValueError:
            url_exists = False
        return url_exists

    def set_attribute_value(self, xpath, value):
        self.execute_script("arguments[0].setAttribute('value',arguments[1])",xpath, value)
        assert MrFix.assertElementIsPresentByXPath_Click(self, xpath), f'Элемента {xpath} на странице нет'

    def open_url_in_new_tab(self, url):
        # open in new tab
        self.execute_script("window.open('%s', '_blank')" % url)
        # Switch to new tab
        self.switch_to.window(self.window_handles[-1])

    def check_clickable_element_and_click(self, xpath_element):
        try:
            element = self.find_element(By.XPATH, xpath_element)
            element.click()
            return True
        except WebDriverException:
            return False

    def make_element_visible_and_click(self, xpath_element):
        while not MrFix.check_clickable_element_and_click(self, xpath_element):
            MrFix.press_down_arrow_key(self, 1)

    def make_element_visible_and_send(self, xpath_element, send_text):
        while not MrFix.check_clickable_element_and_click(self, xpath_element):
            MrFix.press_down_arrow_key(self, 1)
        MrFix.select_and_send_in_input(self, xpath_element, send_text)

    def get_clipboard(self):
        return str(pyperclip.paste())

    def check_visible_element(self, xpath_element):
        try:
            element = self.find_element(By.XPATH, xpath_element)
            return element.is_visible()
        except NoSuchElementException:
            return False

    def check_displayed_element(self, xpath_element):
        try:
            element = self.find_element(By.XPATH, xpath_element)
            return element.is_displayed()
        except NoSuchElementException:
            return False