---
aliases: 
category: 
date modified: 27-07-2025
tags:
  - blank
---
https://github.com/rhyslwells/ML_Tools/blob/main/Explorations/Build/TimeSeries/Forecasting_Baseline.py

Baseline methods are essential for establishing a performance benchmark. They provide insights into the data's underlying patterns and help in assessing the effectiveness of more sophisticated forecasting models. By comparing advanced models against these baselines, you can determine if the added complexity is justified by improved accuracy.

**Methods Implemented:**
    - **Mean Forecasting:** Uses the average of all past values as the forecast for future periods.
    - **Naive Forecasting:** The last observed value is used as the forecast for all future periods.
    - **Seasonal Naive Forecasting:** Uses the value from the previous seasonal period to forecast the future.
    - **Drift Method:** Predicts future values based on the trend between the first and last observations in the training data.