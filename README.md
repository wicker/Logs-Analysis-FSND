# Logs-Analysis-FSND
Logs Analysis project of the Udacity Full Stack Nanodegree

This is an internal reporting tool to get information out of a newspaper site's PostgreSQL database. 

The database has three tables:

- authors (
- articles (
- logs (

The logs.py performs three queries: 

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

# System Requirements

- Python2
- PostgreSQL
- Virtualbox
- Vagrant

# Setup

1. Install the requirements above.

2. Clone this repository and change into the directory.

``` 
git clone https://github.com/wicker/Logs-Analysis-FSND.git
cd Logs-Analysis-FSND
```

3. Bring up the Vagrant machine, which requires about 3.2GB of space. 

```
vagrant up
```

4. When the VM has been created, log into it.

```
vagrant ssh
```

1. Move into the shared vagrant directory.

```
cd /vagrant
```

5. Download and unzip the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file into the `vagrant` directory.

``` 
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
```

7. Connect to andd set up the database server.

```
psql -d news -f newsdata.sql
```

8. Run the logs analysis program from the command line.

```
python newsdata.py
```

# Sample Output (NOT CORRECT YET)

```
What are the most popular three articles of all time?

1. Candidate is jerk, alleges rival
2. Bears love berries, alleges bear
3. Bad things gone, say good people

Who are the most popular article authors of all time?

1. Ursula La Multa
2. Rudolf von Treppenwitz
3. Anonymous Contributor
4. Markoff Chaney

On which days did more than 1% of requests lead to errors?

1. 2016-07-01
2. 2016-07-02
3. 2016-07-03
4. 2016-07-04
5. 2016-07-05

```

# Program Structure


