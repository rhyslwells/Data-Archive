
(Structured Query Language):** Standard language for interacting with ==relational== databases, allowing data queries and manipulation.

Declarative language used to store and query structured data.

A common interface for databases and datalakes

Super underrated. Transactional properties make it fast and powerful to use.



```sql
## Advanced SQL topics you need to know.
# Learn GROUP BYs to aggregate values
SELECT
	MAX(views) AS mostViews,
	channelId
FROM
	YoutubeVideos
GROUP BY
	channelID
;

# Window functions are a must-have for interviews
SELECT
	RANK() OVER(ORDER BY views) AS videoRanking
	videoName,
FROM
	YoutubeVideos
;

# Efficient schema designs go a long way
CREATE TABLE YoutubeVideos (
	videoId INTEGER PRIMARY KEY
	videoName VARCHAR(255),
	views INTEGER,	
	likes INTEGER,
	channelId INTEGER
);
```