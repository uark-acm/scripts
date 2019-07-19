from bs4 import BeautifulSoup
import requests

url = "https://scheduleofclasses.uark.edu/Main"
querystring = {"strm": "1199"}
payload = "campus=FAY&acad_career=UGRD&acad_group=ENGR&subject=CSCE&catalog_nbr1=&catalog_nbr2=&class_section=&session_code=&meeting_time_start_hours=&meeting_time_start_minutes=&meeting_time_start_ampm=&meeting_time_end_hours=&meeting_time_end_minutes=&meeting_time_end_ampm=&room_chrstc=&descr=&last_name=&first_name=&enrl_stat=&class_nbr=&facility_id=&Search=Search&undefined="
headers = {'Content-Type': "application/x-www-form-urlencoded"}
response = requests.request(
    "POST", url, data=payload, headers=headers, params=querystring)


soup = BeautifulSoup(response.text, 'lxml')  # Parse the HTML as a string

table = soup.find_all('table')[0]

rows = []

# get header row
headerRow = []
for row in table.find_all('th'):
    headerRow.append(row.get_text())

rows.append(",".join(headerRow))

for row in table.find_all('tr'):
    dataPoints = []
    for data in row.find_all('td'):
        dataPoints.append(data.get_text())
    rows.append(",".join(dataPoints))

# make the csv file
csvStr = "\n".join(rows)
csvFile = open("class.csv", "w")
csvFile.write(csvStr)
csvFile.close()
