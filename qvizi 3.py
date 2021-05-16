#
# import requests
# lat=35.67
# lon=22.13
# part='hourly'
# key='b6040d22cb226be1f00c4ac79debc6e4'
# url=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}'
# r= requests.get(url)
# print(r.text)
# print(r.status_code)
# print(r.headers['Content-Type'])
# print(r.content)


# import requests
# lat=12.5
# lon=23.6
# cnt=12
# key='b6040d22cb226be1f00c4ac79debc6e4'
# url= f'http://api.openweathermap.org/data/2.5/find?lat={lat}&lon={lon}&cnt={cnt}&appid={key}'
# r= requests.get(url)
# print(r.text)
# print(r.status_code)
# print(r.headers['Content-Type'])
# print(r.content)


# 2
# import requests
# import json
# key='b6040d22cb226be1f00c4ac79debc6e4'
# lat=12.5
# lon=45.2
# cnt=11
# payload={'appid': key, "lat" :lat, "lon":lon, "cnt":cnt }
# r=requests.get('https://api.openweathermap.org/data/2.5/find?', params=payload)
# res=json.loads(r.text)
# print(json.dumps(res, indent=5))

# 3
# import requests
# import json
# import sqlite3
#
# conn=sqlite3.connect('weather_db.sqlite')
# c=conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS weather
#           (max FLOAT ,
#            min FLOAT ,
#            temp FLOAT ,
#            moon FLOAT
#
#
#            ) ''')
#
#
# lat=35.67
# lon=22.13
# part='hourly'
# key='b6040d22cb226be1f00c4ac79debc6e4'
# url=f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}'
# r= requests.get(url)
# res=json.loads(r.text)
# print(json.dumps(res, indent=5))
# print('temperatura:', res['current']['temp'])
# print('wneva:', res['current']['pressure'])
# print('tenianoba:', res['current']['humidity'])
# print('mtvare:', res['daily'][0]['moon_phase'])
# print('minialuri temperatura:', res['daily'][0]['temp']['min'])
# print('maximaluri temperatura:', res['daily'][0]['temp']['max'])
# print('gamis temperatura:', res['daily'][0]['temp']['night'])
#
# with open ('weather.json', 'w') as file:
#     json.dump(res, file, indent=5)
#
# all_rows=[]
# for each in res['daily']:
#     moon=each['moon_phase']
#     temp=each['temp']['night']
#     min=each['temp']['min']
#     max=each ['temp']['max']
#     row=(moon,temp, min, max)
#     all_rows.append(row)
#
#     # print(moon)
#     # print(temp)
#     # print(min)
#     # print(max)
# c.executemany('INSERT INTO weather(moon, temp, min, max ) VALUES (?, ?,?,?)', all_rows)
# conn.commit()
# conn.close()
#

