# Logs-Analysis-FSND

This is an internal reporting tool to get information out of a newspaper site's PostgreSQL database. 

The database has three tables:

- authors (name, bio, id)
- articles (author, title, slug, lead, body, time, id)
- log (path, ip, method, status, time, id)

The Python file newsdata.py performs three queries: 

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

# Setup and Run 

Install the requirements: 

- Python2
- PostgreSQL
- Virtualbox
- Vagrant

Clone this repository and change into the directory.

``` 
git clone https://github.com/wicker/Logs-Analysis-FSND.git
cd Logs-Analysis-FSND
```

Bring up the Vagrant machine, which requires about 3.2GB of space. 

```
vagrant up
```

When the VM has been created, log into it.

```
vagrant ssh
```

Move into the shared vagrant directory.

```
cd /vagrant
```

Download and unzip the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file into the `vagrant` directory.

``` 
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip newsdata.zip
```

Connect to and set up the database server.

```
psql -d news -f newsdata.sql
```

Run the logs analysis program from the command line.

```
python newsdata.py
```

# Program Structure

Each question has its own function with three required pieces:

1. a human-readable printable question to start the output
1. a single SQL query to satisfy the question
1. code to beautify the printed output

The main() connect to the database, runs the questions, and closes the database connection. 

The program can be extended by creating a new question function and calling it in main(). To improve the runtime, question functions can be defined in the program but commented out or otherwise not called in main(). 

# Sample Output

```
The most popular three articles of all time:

  1. Candidate is jerk, alleges rival -- 338647 views
  2. Bears love berries, alleges bear -- 253801 views
  3. Bad things gone, say good people -- 170098 views

Most popular article authors of all time:

  1. Ursula La Multa -- 507594 views
  2. Rudolf von Treppenwitz -- 423457 views
  3. Anonymous Contributor -- 170098 views

Days on which more than 1% of requests led to errors:

  2016-07-17 (2.3%)
```


