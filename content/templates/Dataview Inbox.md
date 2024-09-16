---
tags: productivity
---

https://www.youtube.com/watch?v=8yjNuiSBSAM&ab_channel=FromSergio

https://www.youtube.com/watch?v=ccN5vJzXwvo

### Tasks from a specific header.

- [ ] Use modified task getter 

```
dataviewjs
dv.header(2, 'phd/dailytasks');  
dv.taskList(dv.pages('#phd/dailytasks').file.tasks.filter(task => task.header.subpath == "Phd").where(t => !t.completed));  
```

### Tasks
- [x] Investigate dataview see session buddy
- [x] How to use kaban with dataview? 
- [ ] Make template with dataview prepd

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