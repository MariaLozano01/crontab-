# Crontab-

## Setting up Virtual Machine
Set up GCP environment 

Sudo apt-get update

git clone (Insert Github link)

crontab -h #to check if crontab is already installed

ls -l #to see our files

cd crontab- #to navigate to our .py file with cron job code

nano crontabRead_json.py

crontab -e

insert schedule code needed 

Control key + 'O' to save 
Control key + 'X' to exit the crontab 

systemctl status cron #to check status of crontab code

## Schedule of cron jobs

## Every Sunday at 10pm
0 22 * * SUN /usr/bin/python3 /home/maria_lozano_vargas/crontab-/crontabRead_json.py > log.txt 2>&1 &

## Every Day at 2am
0 2 * * * /usr/bin/python3/home/maria_lozano_vargas/crontab-/crontabRead_json.py > log.txt 2>&1 &

## Pull down data at the end of every quarter
0 0 1 */3 * /usr/bin/python3 /home/maria_lozano_vargas/crontab-/crontabRead_json.py > log.txt 2>&1 &

## To open code needed to schedule cron job
nano crontabRead_json.py

## Restart cron job
sudo service cron reload

## To check status of cron job
systemctl status cron

