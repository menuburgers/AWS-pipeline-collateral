import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ddt import ddt,data,file_data, unpack

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver

#Hook for adding env info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Test Project'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sankha'

#Hook to delete/modify env info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)