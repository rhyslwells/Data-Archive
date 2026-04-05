---
aliases: [BM]
category: INDUSTRY
date modified: 3-04-2026
tags: [balancing, energy, energy_markets, market_design, optimisation, power_markets, power_systems]
---
The **Balancing Mechanism (BM)** is a real-time process operated by [[National Grid ESO|NESO]] to maintain system balance:

$$
Generation(t) = Demand(t) + Losses(t)
$$

It operates from **Gate Closure (1 hour before delivery)** through real time and is the final stage of physical system balancing.

The BM is best understood as a **real-time constrained optimisation process under uncertainty**, implemented through the acceptance of bids and offers.

## Role

Forward and day-ahead markets cannot fully resolve:

- Forecast errors (demand, wind, solar)
- Plant outages
- Network constraints
- Intra-day trading changes

The BM enables [[National Grid ESO|NESO]] to correct these imbalances in real time.

## Key Properties

- No forward commitment required
- Availability declared dynamically
- Actions are based on submitted bids and offers

## Interpretation

- The power system is continuously out of balance
- The BM is the mechanism used to correct this in real time

## Links

- [[Balancing Mechanism Units]]
- [[Bids and Offers (Balancing Mechanism)]]
- [[Balancing Mechanism Operation]]
- [[Imbalance Pricing]]
- [[Elexon]]
- [[Balancing Mechanism Implications]]
- [[Elexon and Settlement]]