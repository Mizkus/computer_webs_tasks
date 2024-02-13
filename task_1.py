import subprocess
import csv


def ping_domain(domain, reps=4):
    out = subprocess.run(['ping', '-c', str(reps), domain], stdout=subprocess.PIPE, text=True)
    for line in out.stdout.split('\n'):
        if 'min/avg/max/mdev' in line:
            return line[line.find('=') + 2:-3].split('/')

with open('task_1.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['domain','min', 'avg', 'max', 'mdev'])
    domains = ['google.com', 'aviasales.ru', 'ok.ru', 'vk.ru', 'nsu.ru', 'github.com', 'mail.ru', 'gmail.com', 'youtube.com', 'yandex.ru']
    for domain in domains:
        writer.writerow([domain] + ping_domain(domain))




