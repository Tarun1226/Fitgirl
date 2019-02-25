import psycopg2, calendar, re

user = 'vqxjdcqueuzpcd'
password = 'c6b5fb0abf7f0e37fbf74b0cd9aa0c37d3805bfa4454beca6dafd86680ba8d1d'
database = 'd1ab7untei66h5'
host = 'ec2-54-235-67-106.compute-1.amazonaws.com'

user_activity_rows = list()

conn = psycopg2.connect(dbname=database, user=user, password=password, host=host)

cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()

cur.execute("SELECT * FROM week_customformsubmission;")
rows = cur.fetchall()

for row in rows:
    (id, form_data, submit_time, page_id, user_id) = row
    cur2.execute("SELECT url_path FROM wagtailcore_page wp WHERE wp.id=(%s);", (page_id,))
    results = cur2.fetchone()
    try:
        (url_path,) = results
    except TypeError:
        continue

    m = re.search('/week-(\d+)/(\w+)/', url_path)
    if m:
        week_number = m[1]
        if re.search('physical', m[2], re.I):
            activity = 'physical'
        elif re.search('nutrition', m[2], re.I):
            activity = 'nutrition'
        else:
            continue

        date = submit_time.date()
        day_of_week = calendar.day_name[date.weekday()]
        points_earned = 1
        cur3.execute("SELECT program_id FROM account_profile WHERE user_id = (%s);", (user_id,))
        try:
            program = cur3.fetchone()[0]
        except TypeError:
            continue

        user_activity_rows.append([activity, week_number, day_of_week, points_earned, date, date, program, user_id])

cur.close()
cur2.close()
cur3.close()

for row in user_activity_rows:
    print(row)

cur = conn.cursor()
try:
    cur.execute('SELECT * FROM user_activity')
except:
    print("Table doesn't exist")
