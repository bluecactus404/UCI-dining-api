from bs4 import BeautifulSoup as BS
import sqlite3

with open('brandy.html', 'r') as f:
    html_doc = f.read()

soup = BS(html_doc, 'html.parser')

soup = soup.find('main', id="main-content")
divs = [s for s in soup.children]

soup_info = divs[0]
soup_meals = divs[1]
soup_meals = soup_meals.find('div', class_='print-menu-container').table.tbody.tr.td
soup_meals = soup_meals.find('div', class_='print-hide')


print(len([section for section in soup_meals.find_all('section')]))
soup_section = soup_meals.find('section')



def get_restraunt_from_section(soup_section:BS) -> str:
    soup_section = soup_section.find('h3')
    return soup_section.string


def get_name_of_dish(soup_li:BS) -> str:
    return soup_li.find('h4').string

def get_description_of_dish(soup_li:BS) -> str:
    return soup_li.find('p').string

def get_num_calories_of_dish(soup_li:BS) -> int:
    string =  soup_li.find_all('span')[1].string
    return string[:string.index(' ')]


"""
Dish dict:
dis_name   -str
dish_picture_url // implement later -str
dish_restraunt -str
dish_vegan -bool
dish_-others //implement later
dish_description  -str
dish_calories   -int
"""

parts = [child for child in soup_section.children]

soup_name = parts[0]

soup_info = parts[1].find('li')
print(get_description_of_dish(soup_info)) 
print(get_num_calories_of_dish(soup_info))
# print(get_restraunt_from_section(parts[0]))

