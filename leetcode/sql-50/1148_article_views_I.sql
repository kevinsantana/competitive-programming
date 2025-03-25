/*
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.
*/

/*
Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.

The result format is in the following example.
*/

WITH ViewedBySelf AS (
    SELECT v.author_id
    FROM Views v
    WHERE v.author_id = v.viewer_id
)

SELECT vbs.author_id AS id
FROM ViewedBySelf vbs
GROUP BY vbs.author_id
ORDER BY vbs.author_id ASC
