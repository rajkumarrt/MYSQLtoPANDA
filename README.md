# MYSQLtoPANDA
Mysql to Panda connectivity 

<h3> MySQL install </h3>
  [MySQL Downlaod] (https://dev.mysql.com/downloads/installer/)
  <p> create DB and table </p>
  
<div class="snippet-clipboard-content position-relative" data-snippet-clipboard-copy-content="MYSQL Managment"><pre><code>
<b> DB Creation </b>
mysql> CREATE DATABASE test;
Query OK, 1 row affected (0.13 sec)

<b> Table Creation </b>
mysql> create table data (id integer(10), name varchar(20), value float(20));
Query OK, 0 rows affected, 1 warning (0.97 sec)

<b> View the Table structure </b>
mysql> desc data;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int         | YES  |     | NULL    |       |
| name  | varchar(20) | YES  |     | NULL    |       |
| value | float       | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
3 rows in set (0.13 sec)

<b> Insert the value </b>
mysql> insert into data values ('1', 'raj', '100.5');
Query OK, 1 row affected (0.13 sec)
</code></pre></div>

<div class="snippet-clipboard-content position-relative" data-snippet-clipboard-copy-content="Package configuration"><pre><code>
<b> Visual studio code </b>
py -m pip install pymysql
py -m pip install mysql-connector-python

<b> Linux </b>
pip install pymysql
pip install mysql-connector-python
</code></pre></div>

Code1 - Data frame
  
Code2 - Dictonary
  
Code3 - Data to CSV
  
