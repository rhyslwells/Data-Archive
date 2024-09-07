

Cant have both.

It is hard to optimize for both simultaneously as optimizing for the False Positives (thereby improving Precision) comes at the expense of the False Negatives (thereby deteriorating Recall), and vice versa.

Task dependant.

Example:

For a spam classification task, it’s probably more desirable to avoid important emails being moved into the spam folder than to have the occasional spam emails going into the inbox. So for this task, we will want to prioritize Precision over Recall.

![[Pasted image 20240116211130.png|500]]