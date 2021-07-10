# executable_path - уберите этот параметр или настройте свой путь до chromedriver
# запуск pytest --language=es test_items.py

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_bt_add_cart(browser):
    browser.get(link)
    browser.find_element_by_css_selector("button.btn-add-to-basket")
