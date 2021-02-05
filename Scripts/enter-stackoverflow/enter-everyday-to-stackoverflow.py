# script to enter stackoverflow has a test and to gain a badge for concurrent visits
# this was built for entertaiment purposes, to learn selenium and unit test package
from selenium.webdriver import Opera
from selenium.webdriver.common.action_chains import ActionChains
import os
import yaml


# get config file and return defined configurations
# WARNING you shouldn't read this from a file or directly
# from the code, try implementing some kind of vault or key manager
def get_cred(directory, file_name):
    cred = {}
    file_name = os.path.join(directory, file_name)
    with open(file_name,'r') as config_file:
        cred = yaml.load(config_file, Loader=yaml.SafeLoader)
    return cred


# initialize driver, open the browser and go to the defined website
def start_browsing(site):
    driver = Opera()
    driver.get(site)
    # be sure we are in stack overflow
    assert 'Stack Overflow' in driver.title, 'It seems like its not Stack Overflow'
    return driver


# enter credentials on logging page to enter the website
def login_to_website(driver,cred):
    try:
        # getting username and password field
        # warning you should abo
        email_box = driver.find_element_by_name('email')
        pass_box = driver.find_element_by_name('password')
        login = driver.find_element_by_name('submit-button')
        # setting an action chains to interact with the website
        # write email and pass and click login to enter website
        actions = ActionChains(driver)
        actions.send_keys_to_element(email_box, cred['U'])
        actions.send_keys_to_element(pass_box, cred['P'])
        actions.move_to_element(login)
        actions.click()
        actions.perform()
        result = 'Daily visit on the site finished.'
    except Exception:
        result = 'Error trying to loggin on the website'
    return result
    
# main function where all gets orchestrated
def main():
    # url where we want to go
    site = 'https://stackoverflow.com/'
    file_name = 'stackoverflow_config.yml'
    working_directory = os.path.dirname('__file__')
    # setting loging url to the site for quicker access
    site = site + 'users/login'
    # get creds
    cred = get_cred(working_directory,file_name)['LOGIN']
    # start browsing
    driver = start_browsing(site)
    # enter and log in on stack overflow
    result = login_to_website(driver, cred)
    print(result)

if __name__ == '__main__':
    main()