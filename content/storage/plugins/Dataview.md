---
tags: []
---

https://www.youtube.com/watch?v=8yjNuiSBSAM&ab_channel=FromSergio

https://www.youtube.com/watch?v=ccN5vJzXwvo

I want to be able to extract all the notes fora given querey. Like the local graph. Maybe so that I can add comments and filter effectively

```dataview-
table
where contains(file.name, ".py")
```

### Get all inline and out links for a given file

```dataview
TABLE
FROM "standardised"
```


### Tasks from a specific header.

- [x] Use modified task getter ✅ 2025-07-20

```
dataviewjs
dv.header(2, 'phd/dailytasks');  
dv.taskList(dv.pages('#phd/dailytasks').file.tasks.filter(task => task.header.subpath == "Phd").where(t => !t.completed));  
```

### Notes

Adding tags to single line and lists will appear in tasks folder

### Kaban: 
```dataview
task from #Gamestonks/active
```

### Set up/ using dataview

[Basis of dataview](https://www.youtube.com/watch?v=7kFEl7Ovsr8&ab_channel=FilipeDonadio)


```dataview
LIST
FROM "uncleaned notes"
SORT file.size DESC
LIMIT 4
```


```dataview
Table author, date
from #todo 
sort size desc
```


```dataview
LIST
FROM "02 Archive"
SORT file.size DESC
LIMIT 10
```


## queries:


```dataview
table author,type
from "02 Archive/Daily"
```