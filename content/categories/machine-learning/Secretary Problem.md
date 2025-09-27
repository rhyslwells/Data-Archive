---
aliases: []
category: ML
date modified: 27-09-2025
tags:
- learning
- optimisation
- probability
- statistics
---
The Secretary Problem (also called the Optimal Stopping Problem) is a classic problem in probability theory and [[Decision Theory]]. It explores the challenge of making an optimal choice when faced with uncertainty and incomplete information.

### Why Care About It?

The Secretary Problem is important because it formalizes ==optimal stopping== decisions under uncertainty, which appear in:

* Hiring decisions (as in the story).
* Real estate (choosing the best property when visiting options sequentially).
* Financial decisions (selling assets, timing investments).
* Online algorithms (ad placement, real-time bidding).
* Resource allocation in data centers or task scheduling.

The key insight: You can't always maximize certainty-you optimize probability given constraints.

### What is the Secretary Problem?

* You have \$n\$ applicants for a job.
* You interview them in random order, one by one.
* After each interview:

  * You know how the candidate ranks among those seen so far (relative rank).
  * You must accept or reject immediately (no recall).
* Goal: Hire the single best applicant overall.
* Question: *What strategy maximizes the probability of choosing the best applicant?*

### Solution Strategy

The optimal solution involves two phases:

1. Observation Phase:

   * Interview and reject the first \$r\$ candidates (where $r \approx \frac{n}{e} \approx 0.37n$).
   * Use them as a sample to set a benchmark for "best so far."
1. Selection Phase:

   * From candidate $r+1$ onward, pick the first applicant who is better than all previous ones.

This gives a maximum success probability of about:

$$
P(\text{success}) \approx \frac{1}{e} \approx 36.8\%
$$



