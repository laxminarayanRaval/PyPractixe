import requests
from bs4 import BeautifulSoup

list_data = dict()
sub_date = dict()
url = "https://ums.vnsgu.net/Result/StudentResultDisplay.aspx?HtmlURL=1962,2020052191"
page_data = requests.get(url).text

# print(page_data)

soup = BeautifulSoup(page_data, 'html.parser')
for table in soup.find_all('table'):
    print(table.get('class'))

table = soup.find('table', class_='maintbl')
#
# col = ''
# for row in table.tbody.find_all('tr'):
#     columns = row.find_all('td')
#     if columns != []:
#         for column in columns:
#             if col == 'SP ID:' or col == 'Student Name:' or col == 'Total Marks :':
#                 list_data[col] = column.text.strip()
#             col = column.text.strip()
#             # print(column)

fields = ['Student Name', 'SP ID', 'INTERNET OF THINGS', 'DESIGN PATTERNS', 'ADVANCED JAVA PROGRAMMING',
          'FULL STACK TECHNOLOGY', 'OPEN SOURCE WEB BASED PROGRAMMING', 'PROGRAMMING SKILLS-VIII',
          'PROGRAMMING SKILLS-IX', 'PROGRAMMING SKILLS-X', 'PROGRAMMING SKILLS-XI',
          "Total Marks", 'SGPA', 'YGPA', 'Result', '']
sub_fields = ['INTERNET OF THINGS', 'DESIGN PATTERNS', 'ADVANCED JAVA PROGRAMMING',
              'FULL STACK TECHNOLOGY', 'OPEN SOURCE WEB BASED PROGRAMMING', 'PROGRAMMING SKILLS-VIII',
              'PROGRAMMING SKILLS-IX', 'PROGRAMMING SKILLS-X', 'PROGRAMMING SKILLS-XI', ]

subtable = soup.find('table', class_='maintbl subtable')
i = 0
j = 0
for row in table.tbody.find_all('tr'):
    if row.text.startswith(fields[i]):
        columns = row.find_all('td')
        i += 1
        if columns != []:
            for column in columns:
                #     list_data[col] = column.text.strip()
                # if col == 'SP ID:' or col == 'Student Name:' or col == 'Total Marks :':
                if column.text:
                    col = column.text.strip()
                    # if fields[i] == sub_fields[j]:
                        # list_data[fields[i]] = col
                    print("__", i, "___", col)

        print(row.text)
# print(list_data)
# {
#   'spid', 'student name',
#   'sub_marks':[{sub_name, ext_mrks, int_mrks, ttl_mrks, gl, gp}],
#   'ttl_mrks', 'sgpa', 'ygpa', 'result'
#   }
