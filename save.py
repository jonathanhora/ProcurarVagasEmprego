import csv

def save_to_csv(all_jobs):
  file = open('all_jobs.csv','w')
  writer = csv.writer(file)
  writer.writerow(['title', 'company', 'location', 'how_old', 'link_job'])
  for job in all_jobs:
     writer.writerow(list(job.values()))
