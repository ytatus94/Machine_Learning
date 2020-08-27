# BitTiger DS501 Week4

## SQL

### SQL Basic

* SELECT
* FROM
* WHERE
* LIKE
* GROUP BY
* HAVING
* ORDER BY

### SQL Intermediate

* JOIN
* DISTINCT
* UNION
* COALESCE
* TEMP TABLE
* WITH

### SQL Advanced

* SELF JOIN
* CASE WHEN
* IF
* OVER PARTITION BY
* DATE FUNCTION

---

### SQL Introduction

* SQL: Structured Query Language
* RDBMS: Relational DataBase Management System
  * 有 PostgreSQL, SQLite, MySQL, MSSQL, Oracle 等等
* NoSQL: Not Only SQL
  * 是用 document based, key-value pairs, graph databases, 或是 wide-column 的方式儲存
    * Hadoop/Hbase: wide-column
    * MongoDB: document based
    * Neo4j: graph databases
  * Document based 通常是 json 格式
* 型態有：
  * 字元：CHAR(20), VARCHAR(50)
    * 括號內的數字是指定字元的長度
  * 數字：INT, BIGINT, SMALLINT, FLOAT
  * 其他：MONEY, DATETIME, 等等
* Primary key 和 Foreign key:
  * Primary key: 表格中每一列的 id，是唯一的值
  * Foreign key: 其他表格中的 primary key

What is the difference between primary key and foreign key?

---

### SQL Syntax

```SQL
SELECT column_name1, column_name2
FROM table_name
WHERE condition
GROUP BY column_name3
HAVING aggregated condition
ORDER BY column_name4 ASC/DESC
LIMIT n;
```

* SQL 命令的順序很重要：
WHERE -> GROUP BY -> HAVING -> ORDER BY -> LIMIT
  * WHERE 是對一般的列做條件判斷
  * HAVING 是對 aggregated 後的做條件判斷
  * ORDER BY 預設是用遞增排序 (ASC)
* SQL 命令是不區分大小寫的，但習慣上都用大寫
* SELECT 的用法範例：

```SQL
SELECT *
SELECT a1, a2, a3
SELECT a1 AS b1, a2 AS b2
SELECT a1+a2 AS b1, a1-a1*a2/a3 AS b2
SELECT DISTINCT a1, a2, a3
SELECT aggregate_function
```

* WHERE 條件判斷可以使用的邏輯運算有：
  * >, <, =, != 或 <>, LIKE, BETWEEN, IN, IS NULL, IS NOT NULL, AND, OR, NOT 
  * LIKE 可以使用通配符
  * _ 是代表一個字元
  * % 是代表很多個字元
  * %plus 是表示以 plus 結尾，plus% 表示以 plus 開頭，%plus% 表示有 plus 在中間，pl_s 表示 pl 開頭 s 結尾的四個字元
* Aggregate functions 有
  * MIN() / MAX()
  * SUM()
  * AVG()
  * COUNT() / COUNT(*)

* Product 表格：

|PName|Price|Category|Manufacturer|
|:--:|:--:|:--:|:--:|
|Gizmo|$19.99|Gadgets|Gizmo Works|
|Powergizmo|$29.99|Gadgets|Gizmo Works|
|SingleTouch|$149.99|Photography|Canon|
|MultiTouch|$203.99|Household|Hitachi|

```SQL
SELECT *
FROM Product
WHERE Category = 'Gadgets';
```
結果會是

|PName|Price|Category|Manufacturer|
|:--:|:--:|:--:|:--:|
|Gizmo|$19.99|Gadgets|Gizmo Works|
|Powergizmo|$29.99|Gadgets|Gizmo Works|

* GROUP BY 範例
* Purchase 表格：

|Product|Date|Price|Quantity|
|:--:|:--:|:--:|:--:|
|Bagel|10/21|1|20|
|Bagel|10/25|1.50|20|
|Banana|10/3|0.5|10|
|Banana|10/10|1|10|

```SQL
SELECT Product, SUM(Price * Quantity) AS TotalSales
FROM Purchase
WHERE Date > '10/1/2005'
GROUP BY Product
```

結果是

|Product|TotalSales|
|:--:|:--:|
|Bagel|50|
|Banana|15|

* HAVING 範例
HAVING 的條件不一定要出現在 SELECT 裡面

What is the difference between WHERE and HAVING?

```SQL
SELECT Product, SUM(Price * Quantity) AS TotalSales
FROM Purchase
WHERE Date > '10/1/2005'
GROUP BY Product
HAVING SUM(quantity) > 30
```

### SQL intermediate syntax

* **INNER JOIN**：兩個表格共同都有的才會合併
* **LEFT JOIN**：左邊表格全部都保留，右邊表格只有符合的才合併，沒符合的部分用 NULL 取代
* **RIGHT JOIN**：右邊表格全部都保留，左邊表格只有符合的才合併，沒符合的部分用 NULL 取代
* **FULL JOIN**：左邊表格和右邊表格都全部保留，沒有符合的部分用 NULL 取代
* **OUTER JOIN**: `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN` 都屬於 `OUTER JOIN`

What is the difference between INNER JOIN and LEFT JOIN?

T1 表格

|ID|Age|
|:--:|:--:|
|1|15|
|2|16|

T2 表格

|ID|Grade|
|:--:|:--:|
|1|98|
|3|80|

T3 表格

|ID|Grade|Subject|
|:--:|:--:|:--:|
|1|98|Chinese|
|3|80|Chinese|
|3|90|Maths|

`INNER JOIN`

```SQL
SELECT *
FROM T1
INNER JOIN T2
   ON T1.ID = T2.ID
```

|ID|Age|ID|Grade|
|:--:|:--:|:--:|:--:|
|1|15|1|98|


`LEFT JOIN`

```SQL
SELECT *
FROM T1
LEFT JOIN T2
  ON T1.ID = T2.ID
```

|ID|Age|ID|Grade|
|:--:|:--:|:--:|:--:|
|1|15|1|98|
|2|16|NULL|NULL|

`RIGHT JOIN`

```SQL
SELECT *
FROM T1
RIGHT JOIN T2
   ON T1.ID = T2.ID
```

|ID|Age|ID|Grade|
|:--:|:--:|:--:|:--:|
|1|15|1|98|
|NULL|NULL|3|80|

`FULL JOIN`

```SQL
SELECT *
FROM T1
FULL JOIN T2
  ON T1.ID = T2.ID
```

|ID|Age|ID|Grade|
|:--:|:--:|:--:|:--:|
|1|15|1|98|
|2|16|NULL|NULL|
|NULL|NULL|3|80|

```SQL
SELECT COUNT(*) AS total_count
FROM T1
INNER JOIN T3
   ON T1.ID = T3.ID
```

|ID|Age|ID|Grade|
|:--:|:--:|:--:|:--:|
|1|15|1|98|
|3|16|3|80|
|3|16|3|90|

```SQL
SELECT COUNT(DISTINCT T1.ID) AS total_count
FROM T1
INNER JOIN T3
   ON T1.ID = T3.ID
```

SELECT DISTINCT column1, column2
FROM table_name;

SELECT COUNT(DISTINCT column)
FROM table_name;

Count distinct without using DISTINCt()

```SQL
SELECT COUNT(*)
FROM (
      SELECT customer_id
      FROM table
      GROUP BY 1);
```

```SQL
SELECT COUNT(DISTINCT customer_id)
FROM table;
```

`SELECT COUNT(DISTINCT id)` What is the more efficient way to achieve `COUNT(DISTINCT id)`?
A: `SELECT COUNT(1) FROM (SELECT id FROM table GROUP BY 1);`


UNION and UNION ALL

* UNION 把兩個 table 上下疊起來，不顯示重複的列
* UNION ALL 才會顯示重複的列

What is the difference between UNION and JOIN?

What is the difference between UNION and UNION ALL

```SQL
SELECT column1, column2 FROM table1
UNION
SELECT column1, column2 FROM table2;
```

```
SQL
SELECT column1, column2 FROM table1
UNION ALL
SELECT column1, column2 FROM table2;
```

NBA1 表格

|FirstName|LastName|Age|
|:--:|:--:|:--:|
|Kobe|Bryant|40|
|Michael|Jordan|50|

NBA2 表格

|FirstName|LastName|Age|
|:--:|:--:|:--:|
|Kobe|Bryant|40|
|Tim|Duncan|42|

```SQL
SELECT * FROM NBA1
UNION
SELECT * FROM NBA2
```

|FirstName|LastName|Age|
|:--:|:--:|:--:|
|Kobe|Bryant|40|
|Michael|Jordan|50|
|Tim|Duncan|42|

```SQL
SELECT * FROM NBA1
UNION ALL
SELECT * FROM NBA2
```
|FirstName|LastName|Age|
|:--:|:--:|:--:|
|Kobe|Bryant|40|
|Michael|Jordan|50|
|Kobe|Bryant|40|
|Tim|Duncan|42|

COALESCE: Set default value if missing
COALESCE 連結，接合，傷口癒合

```SQL
SELECT COALESCE(s.spend, 0) AS spend
FROM user AS u
LEFT OUTER JOIN spend AS s
  ON u.tsid = s.tsid
```

CTE: common table expression
用 WITH

```SQL
WITH cte1 (column1, column2) AS (SELECT...),
     cte2 (column1, column2) AS (SELECT...)
SELECT ...
```

```SQL
WITH Sales_CTE (SalesPersonID, SalesOrderID) AS (
    SELECT SalesPersonID, SalesOrderID
    FROM Sales.SalesOrderHeader
    WHERE SalesPersonID IS NOT NULL
)
SELECT SalesPersonID, COUNT(SalesOrderID) AS TotalSales
FROM Sales_CTE
GROUP BY 1;
```

Temp table:
* 用 SELECT ... INTO
* 比 subquery 好讀

What is the difference between a view table and a temp table?

```SQL
SELECT column
INTO newtable
FROM table
```


```SQL
SELECT *
FROM table1
WHERE user_id IN (
    SELECT user_id
    FROM order
    WHERE order_id IN (
        SELECT order_id
        FROM product_table
        WHERE ...
        )
    );
    
SELECT order_id
INTO order_temp
FROM product_table
WHERE ...;

SELECT user_id
INTO user_temp
FROM order AS o1
INNER JOIN order_temp AS ot
   ON o1.order_id = ot.order_id;
```

Self Join

Category 表格

|Category_ID|Category_Name|Parent_Category_ID|
|:--:|:--:|:--:|
|1|Cars|NULL|
|2|Honda|1|
|3|Toyota|1|
|4|Flowers|NULL|
|5|Lily|4|
|6|Rose|4|
|7|Sakura|4|

Count how many category instances do each parent category name have?

```SQL
SELECT c2.Category_Name, COUNT(1) AS count
FROM category AS c1
LEFT JOIN category AS c2
  ON c1.Parent_Category_ID = c2.Category_ID
GROUP BY 1
```

|Category_ID|Category_Name|Parent_Category_ID|Category_ID|Category_Name|Parent_Category_ID|
|:--:|:--:|:--:|:--:|:--:|:--:|
|1|Cars|NULL|NULL|NULL|NULL|
|2|Honda|1|1|Cars|NULL|
|3|Toyota|1|1|Cars|NULL|
|4|Flowers|NULL|NULL|NULL|NULL|
|5|Lily|4|4|Flowers|NULL|
|6|Rose|4|4|Flowers|NULL|
|7|Sakura|4|4|Flowers|NULL|

Count how many category instances do each top category have?

```SQL
SELECT t2.Category_ID, COUNT(1) AS count
FROM category AS t1
INNER JOIN category AS t2
   ON t1.Parent_Category_ID = t2.Category_ID
WHERE t2.Category_ID IS NOT NULL
GROUP BY 1;
```

CASE WHEN

```SQL
SELECT CASE (column
