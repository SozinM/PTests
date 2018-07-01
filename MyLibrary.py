from selenium import webdriver
import time


class MyLibrary():

    def __init__(self): #TODO: check other browsers
        self.webdriver_list = ['Firefox','Chrome','Ie','Opera']
        self.total_entryes = 11
        self.unsupported_entryes = 8

    def open_browser(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def close_browser(self):
        self.driver.close()

    def test_title(self,page_title):
        assert self.driver.title == page_title

    def test_entries(self):
        table = self.driver.find_element_by_xpath('//*[@id="download"]/div[4]/div[1]/table[1]').text.split('\n')
        assert len(table) == self.total_entryes

    def test_main_table_class(self,class_name):
        table_class = self.driver.find_element_by_xpath('//*[@id="download"]/div[4]/div[1]/table[1]').get_attribute('class')
        assert table_class == class_name

    def test_unsupported_class(self, unsupported_class):
        for entry_number in range(self.total_entryes+1-self.unsupported_entryes,self.total_entryes+1): #find last 8 entryes in table
            entry = self.driver.find_element_by_xpath('//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%d]'%(entry_number)).get_attribute('class')
            assert entry == unsupported_class

    def format_versions(self,version):
        '''Format version to x.x and x.x.x format'''
        version = version.replace(' LTS 3','').replace(' LTS','')
        version = version.split(' ')
        return version[0],version[1]

    def test_versions_numbers_splitted_by_dots(self):
        for entry_number in range(2,self.total_entryes + 1): #cause xpath runs from 1
            entry = self.driver.find_element_by_xpath(
                '//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%d]'%(entry_number)).text # TODO: use more detailed XPath
            ReleaseSeries, LastRelease = self.format_versions(entry)
            assert len(ReleaseSeries.split('.')) == 2 #there is 2 numbers in Release Series
            assert len(LastRelease.split('.')) == 3 #there is 3 numbers in Last release

    def test_versions_numbers(self):
        for entry_number in range(2, self.total_entryes + 1): #cause xpath runs from 1
            entry = self.driver.find_element_by_xpath(
                '//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%d]' % (entry_number)).text # TODO: use more detailed XPath
            ReleaseSeries, LastRelease = self.format_versions(entry)
            for number in ReleaseSeries.split('.') + LastRelease.split('.'): #check all the numbers
                assert isinstance(int(number),int) #just int(i) throw exception

    def test_versions_substring(self):
        for entry_number in range(2, self.total_entryes + 1): #cause xpath runs from 1
            entry = self.driver.find_element_by_xpath(
                '//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%d]' % (entry_number)).text # TODO: use more detailed XPath
            ReleaseSeries, LastRelease = self.format_versions(entry)
            release_main, release_second = ReleaseSeries.split('.')
            version_main,version_second,version_third = LastRelease.split('.')
            assert (release_main == version_main) and (release_second == version_second)

    def test_date_logic(self):
        for entry_number in range(2, self.total_entryes+1):  #cause xpath runs from 1
            EndOfMainstream = self.driver.find_element_by_xpath('//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%s]/td[3]' % (entry_number)).text
            EndOfExtended = self.driver.find_element_by_xpath('//*[@id="download"]/div[4]/div[1]/table[1]/tbody/tr[%s]/td[4]' % (entry_number)).text
            EndOfMainstream = self.string_date_to_time(EndOfMainstream)
            EndOfExtended = self.string_date_to_time(EndOfExtended)
            assert EndOfMainstream < EndOfExtended

    def string_date_to_time(self,date):
        '''converting date to format Aug 30 17'''
        date = date.replace(unicode('Until at least '), '').replace(unicode(','), '')
        date = date.split(' ')
        if len(date) == 3:
            return time.strptime('%s %d %d'%(date[0][0:3],int(date[1]),int(date[2][2:4])),"%b %d %y")
        else:
            return time.strptime('%s %d %d'%(date[0][0:3],1,int(date[1][2:4])),"%b %d %y")
