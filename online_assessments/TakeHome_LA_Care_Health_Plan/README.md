# Data Scientist Screening Exercise

## Data
This repository's [model_outcome.csv](https://github.com/screening-lacare/data_scientist_screening/blob/master/model_outcome.csv) file contains the ficticious results of a classification model. The three fields included in the file are:
- `index` : The unique ID of each observation.
- `class` : The true class of each observation. The classes are binary (0 or 1).
- `predicted_prob` : The model's estimate of probability that the observation belongs to `class` 1. 

## Instructions
Using the [model_outcome.csv](https://github.com/screening-lacare/data_scientist_screening/blob/master/model_outcome.csv), develop either an R or Python script to:
1. _*Manually*_ calculate the sensitivity and specificity of the model, using a `predicted_prob` threshold of greater than or equal to .5. 
2. _*Manually*_ calculate the Area Under the Receiver Operating Characteristic Curve.
3. Visualize the Receiver Operating Characterstic Curve.
4. Email your finalized, completely reproducible .r or .py script to L.A. Care's Talent Acquisition Specialist, Jamessa Jones, at jjones@lacare.org.

## Assessment
In addition to formulating the correct outputs for the above-mentioned requirements, the applicant's script will be assessed on:
- Coding Style
- Commenting Effectiveness
