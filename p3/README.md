# Udacity Logs Analysis Project
>K M A
### About

This project is a simple CLI reporting tool based on tables in a PostgreSQL database.
The tool runs three reports for answers to the following questions:
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

### Requirements
* Python3
* PostgreSQL
* Vagrant
* Virtual Box

### Installation

1. connect to the virtual machine
```
$ vagrant up
$ vagrant ssh
$ cd /vagrant
```
2. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip this file after downloading it. The file inside is called *newsdata.sql*. Put this file into the vagrant directory, which is shared with the virtual machine. Setup and load the data.
```
ubuntu@ubuntu-xenial:~$ cd /vagrant
ubuntu@ubuntu-xenial:/vagrant$ psql -d news -f newsdata.sql
```
3. Run the code print results
```sh
ubuntu@ubuntu-xenial:/vagrant$ python3 newsdata.py
```

### Output
```
                Start

 The most popular three articles of all time:
 ---------------------------------------------

   *Candidate is jerk, alleges rival - 338647 views
   *Bears love berries, alleges bear - 253801 views
   *Bad things gone, say good people - 170098 views

 The most popular article authors of all time:
 ---------------------------------------------

   *Ursula La Multa - 507594 views
   *Rudolf von Treppenwitz - 423457 views
   *Anonymous Contributor - 170098 views
   *Markoff Chaney - 84557 views

 Days with more than 1% of requests that lead to errors:
 -------------------------------------------------------

   *July 17, 2016 - 2.26% errors

                 End

```


