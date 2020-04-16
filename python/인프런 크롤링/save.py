import csv

def save_to_file(jobs):
    file = open("jobs.csv",mode='w',encoding='utf-8',newline="")
    writer = csv.writer(file)
    writer.writerow(['강의명', '범주', '평점', '가격','링크'])
    for job in jobs:
         writer.writerow(list(job.values()))
    return