from selenium import webdriver
import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description='POIS Questionnaire Filler', formatter_class=RawTextHelpFormatter)
parser.add_argument("-b","--browser", choices = ['c','f'], help="select browser Google Chrome(c)/Firefox(f), by default Chrome", default='c')
parser.add_argument("-u","--username", help="<name.surname>", required=True)
parser.add_argument("-p","--password", help="<password>", required=True)
parser.add_argument("-t","--type", help="research(r)/students(s) account, by default research(r)", default='r')
parser.add_argument("-o","--option", type=int,choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], help="""(1) Did Nothing
(2) Self discovery 
(3) Reading/Learning from some outside source (books, wiki, YouTube etc) 
(4) Brainstorming with friends 
(5) Intersection of (2) & (3) 
(6) Intersection of (2) & (4) 
(7) Intersection of (3) & (4) 
(8) All of (2), (3) and (4) 
(9) Couldn't find time 
(10) Not interested in the course

By default (1) Did Nothing""", default=1)

args = parser.parse_args()

if args.browser == 'c':
	driver = webdriver.Chrome()
else:
	driver = webdriver.Firefox()

driver.get('https://moodle.iiit.ac.in/login/index.php?authCAS=CAS')

uname = args.username + '@' + args.type
username = driver.find_element_by_id("username")
username.clear()
username.send_keys(uname)

password = driver.find_element_by_id("password")
password.clear()
password.send_keys(args.password)

driver.find_element_by_name("submit").click()

driver.find_element_by_link_text("Principles of Information Security").click()
driver.find_element_by_link_text("Questionnaire").click()
driver.find_element_by_link_text("Answer the questions...").click()

opt = 'auto-rb{:04d}'.format(args.option)
# print(opt)
driver.find_element_by_id(opt).click()
driver.find_element_by_name("submit").click()
