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
<p> py -m pip install pymysql
py -m pip install mysql-connector-python </p>
<b> Linux </b>
<p> pip install pymysql
pip install mysql-connector-python </p>
</code></pre></div>


<p><a href="https://github.com/rajkumarrt/MYSQLtoPANDA/blob/main/mysql_dataframe.py"> Code1 - Data frame </a>&nbsp;</p>
  
<p><a href="https://github.com/rajkumarrt/MYSQLtoPANDA/blob/main/mysql_dict.py"> Code2 - Dictonary </a>&nbsp;</p>
  
<p><a href="https://github.com/rajkumarrt/MYSQLtoPANDA/blob/main/MYSQL_CSV.py"> Code3 - Data to CSV </a>&nbsp;</p>

<div class="snippet-clipboard-content position-relative" data-snippet-clipboard-copy-content=" Note: Exporting Data "><pre><code>
<p>
# df.to_csv(filename) -> Writes to a CSV file
# df.to_excel(filename) -> Writes on an Excel file
# df.to_sql(table_name, connection_object) -> Writes to a SQL table
# df.to_json(filename) -> Writes to a file in JSON format
# df.to_html(filename) -> Saves as an HTML table
# df.to_clipboard() -> Writes to the clipboard
  </p> </code></pre></div>

  
