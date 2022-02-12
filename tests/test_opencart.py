import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slideshow(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    slideshow = wait.until(EC.visibility_of_element_located((By.ID, "slideshow0")))
    assert slideshow


def test_search(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    button_search = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search > span > button")))
    button_search.click()
    assert button_search

def test_cart(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    button_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#cart > button")))
    button_cart.click()
    assert button_cart


def test_site_map(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5)
    site_map = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body > footer > div > div > div:nth-child(2) > ul > li:nth-child(3) > a")))
    site_map.click()
    assert site_map

def test_currency(browser):
        browser.get(browser.url)
        wait = WebDriverWait(browser, 5)
        currency = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency > div > button")))
        currency.click()
        assert currency


def test_catalog_sort(browser):
    catalog_url = "index.php?route=product/category&path=20"
    browser.get(browser.url + catalog_url)
    wait = WebDriverWait(browser, 5)
    sort_catalog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-sort")))
    sort_catalog.click()
    assert sort_catalog


def test_catalog_show(browser):
    catalog_url = "index.php?route=product/category&path=20"
    browser.get(browser.url + catalog_url)
    wait = WebDriverWait(browser, 5)
    show_catalog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-limit")))
    show_catalog.click()
    assert show_catalog


def test_wishlist(browser):
    catalog_url = "index.php?route=product/category&path=20"
    browser.get(browser.url + catalog_url)
    wait = WebDriverWait(browser, 5)
    add_wishlist = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group > button:nth-child(2)")))
    add_wishlist.click()
    assert add_wishlist

def test_add_to_cart(browser):
    catalog_url = "index.php?route=product/category&path=20"
    browser.get(browser.url + catalog_url)
    wait = WebDriverWait(browser, 5)
    add_in_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div:nth-child(7) > div:nth-child(2) > div > div:nth-child(2) > div.button-group > button:nth-child(1)")))
    add_in_cart.click()
    assert add_in_cart


def test_list_catalog(browser):
    catalog_url = "index.php?route=product/category&path=20"
    browser.get(browser.url + catalog_url)
    wait = WebDriverWait(browser, 5)
    grid_catalog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#grid-view")))
    grid_catalog.click()
    assert grid_catalog



def test_product_in_cart(browser):
    product_url = "index.php?route=product/product&product_id=43"
    browser.get(browser.url + product_url)
    wait = WebDriverWait(browser, 5)
    product_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#button-cart")))
    product_cart.click()
    assert product_cart


def test_write_review(browser):
    product_url = "index.php?route=product/product&product_id=43"
    browser.get(browser.url + product_url)
    wait = WebDriverWait(browser, 5)
    review = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.rating > p > a:nth-child(7)")))
    review.click()
    assert review


def test_compare_product(browser):
    product_url = "index.php?route=product/product&product_id=43"
    browser.get(browser.url + product_url)
    wait = WebDriverWait(browser, 5)
    product_compare = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.btn-group > button:nth-child(2)")))
    product_compare.click()
    assert product_compare



def test_share_product(browser):
    product_url = "index.php?route=product/product&product_id=43"
    browser.get(browser.url + product_url)
    wait = WebDriverWait(browser, 5)
    product_share = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div.col-sm-4 > div.rating > div > a.addthis_counter.addthis_pill_style.addthis_nonzero > a.atc_s.addthis_button_compact")))
    product_share.click()
    assert product_share


def test_product_image(browser):
    product_url = "index.php?route=product/product&product_id=43"
    browser.get(browser.url + product_url)
    wait = WebDriverWait(browser, 5)
    image_tap = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(3) > a > img")))
    image_tap.click()
    assert image_tap



def test_registration_continue(browser):
    register_url = "index.php?route=account/register"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    continue_registration = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")))
    continue_registration.click()
    assert continue_registration


def test_privacy(browser):
    register_url = "index.php?route=account/register"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    privacy_policy = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")))
    privacy_policy.click()
    assert privacy_policy


def test_login_page(browser):
    register_url = "index.php?route=account/register"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    login_to_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > p > a")))
    login_to_page.click()
    assert login_to_page


def test_forgot_password(browser):
    register_url = "index.php?route=account/register"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    password_forgotten = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-right > div > a:nth-child(3)")))
    password_forgotten.click()
    assert password_forgotten



def test_homepage(browser):
    register_url = "index.php?route=account/register"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    to_homepage = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#account-register > ul > li:nth-child(1) > a > i")))
    to_homepage.click()
    assert to_homepage



def test_login_admin(browser):
    register_url = "admin"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    admin_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")))
    admin_login.click()
    assert admin_login


def test_admin_password_forget(browser):
    register_url = "admin"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    admin_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a")))
    admin_login.click()
    assert admin_login



def test_admin_catalog(browser):
    register_url = "admin"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    admin_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")))
    admin_login.click()
    catalog_admin = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-catalog > a")))
    catalog_admin.click()
    assert catalog_admin


def test_admin_to_main(browser):
    register_url = "admin"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    admin_login = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div.text-right > button")))
    admin_login.click()
    main_page = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer > a")))
    main_page.click()
    assert main_page


def test_admin_username(browser):
    register_url = "admin"
    browser.get(browser.url + register_url)
    wait = WebDriverWait(browser, 5)
    admin_username = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))
    admin_username.click()
    assert admin_username
