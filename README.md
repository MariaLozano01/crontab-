# Crontab-

## Setting up Virtual Machine

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

