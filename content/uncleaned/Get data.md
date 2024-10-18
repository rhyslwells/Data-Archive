---
type: process
tags:
  - ml
---
# What is involved:

`df = pd.read_csv('Categorical.csv')`

- Gather relevant data from appropriate sources, addressing any quality or privacy concerns.

```python
## Get textbook data using for example:

import re
def read_file(filename):
    with open(filename, "r", encoding='UTF-8') as file:
        contents = file.read().replace('\n\n',' ').replace('[edit]', '').replace('\ufeff', '').replace('\n', ' ').replace('\u3000', ' ')
    return contents
text = read_file('Data various/Monte_Cristo.txt')

text_start = [m.start() for m in re.finditer('VOLUME ONE', text)]
text_end = [m.start() for m in re.finditer('End of Project Gutenberg', text)]
text = text[text_start[1]:text_end[0]]
```


How would you approach a colleague who is hesitant to share their data?
?
- explain the purpose and benefits
- ensure confidentiality (GDPR) with data masking.
- and finding common ground to address any concerns or objections.
- build trust.
- make agreements of terms of use/ownership/document the data accessing process.

How would you go about obtaining the necessary permissions for a dataset?
?
- establishing clear communication channels within the organsisation.
- obtaining necessary approvals
- emphasizing the value of collaboration.

How would you gather sensitive data?;; Get consent. Ensure anonyminaty (follow regularions)

How to you ensure data is unbiased and representative.
?
- Stratified sampling, (group then randomly sample).
- Examine the data sources.