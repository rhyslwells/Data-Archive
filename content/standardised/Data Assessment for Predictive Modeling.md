### Data assessment vs data visualization

Data assessment is focused on checking the suitability of data for predictive modeling and planning for data preparation, rather than communicating results to an audience.

Focus on Internal Analysis: The analyses during data assessment are meant for internal use to understand and improve the data, not for external communication.

Use of Graphics: While graphics are used in data assessment, their purpose is to help understand the data's limitations and dynamics, not to present findings to others.

This video emphasizes the importance of assessing data quality and readiness before moving on to data visualization and communication.

Edward Tufte - author

### Data assessment in practice
#data_understanding

"Introducing the critical data understanding phase of CRISP-DM":

- Data Understanding Phase: This phase is crucial in the CRISP-DM process, focusing on assembling and understanding the data before moving to data preparation.
- Uncovering Hidden Patterns: The goal is to uncover hidden patterns in the data that can be revealed through data preparation, aiding the modeling algorithms.
- Supervised Machine Learning: The focus is on building predictive models using supervised machine learning, which is more commonly deployed compared to unsupervised models.

This phase ensures that the data is suitable and ready for the subsequent steps in the data mining process.

CRISP-DM stands for the Cross-Industry Standard Process for Data Mining. It is a widely used methodology for data mining projects, consisting of six phases:  
  
1. Business Understanding: Understanding the project objectives and requirements from a business perspective.
2. Data Understanding: Collecting and understanding the data, identifying data quality issues, and uncovering hidden patterns.
3. Data Preparation: Preparing the final dataset for modeling by selecting, cleaning, and transforming data.
4. Modeling: Applying various modeling techniques to the prepared data and selecting the best models.
5. Evaluation: Evaluating the models to ensure they meet business objectives.
6. Deployment: Deploying the model in a real-world scenario to make predictions or gain insights.

### Data mining

Data mining refers to the process of discovering useful patterns and insights from large datasets. In the context of CRISP-DM, it involves:  
- Finding Useful Patterns: Identifying patterns in the data that can be used to make predictions or gain insights.
- Building Predictive Models: Using these patterns to create models that can predict future outcomes or behaviors.

The term "data mining" has evolved and is now often referred to as traditional machine learning, particularly focusing on supervised machine learning where models are built to make predictions based on labeled data.

### Buisness Understanding phase

using data models, data dictionaries, metadata.
Personel understanding,
software exisitng.
how the buinsess meausre success
Translating buiness objectives into the model. 
develop plan

## Project management of data 

Describe the data
Explore the data
Data Prep
Verifiy data quality.

### Formal reports for Data Preparation

Summary of understand for data understanding.

"Why formal reports are important":  
  
- Documentation is crucial: Formal reports at the end of each phase in the CRISP-DM process are essential for ==measuring progress== and ==preparing for deployment (and to be productionised).==
- Long-term value: Well-documented reports can be valuable for years, as they provide detailed insights and can be referenced long after the project is completed.
- Content of reports: Each report should include data sources, methods of acquisition, problems encountered, patterns found, and data quality assessments. This information is vital for data preparation and eventual deployment.

Reports:
- Initial Data Collection Report: Includes a list of data sources, methods of acquisition, extraction details, and any problems encountered.
- Data Description Report: Describes each data source in detail, including field descriptions and implications for data integration.
- Data Exploration Report: Documents regularities or patterns found, both expected and unexpected, surprises or quirks, and conclusions for data transformation, cleaning, and pre-processing. And discussions with SMEs.
- Data Quality Report: Summarizes the approach taken to assess data quality, findings, and conclusions, which feed into the data preparation phase.

### Data Preparation

- Data Prep Tasks: There are five key data preparation tasks influenced by the [[data understanding]] phase, including data integration and handling missing data.
- Iterative Phases: The phases of data understanding and data preparation overlap and iterate, meaning they don't come to a complete stop before moving on.
- Importance of Data Understanding: Proper data understanding is critical for successful data preparation, helping to identify what needs attention and how to handle data integration and missing data issues effectively.

[[data understanding]] feeds into [[Obsidian-Integration-main/Data Preparation]] by making a check list for it.


### [[data understanding]]

Get a sense for the data we want.

To discard variables.


### [[Obsidian-Integration-main/Data Preparation]]

Should have a checklist of what we are going to do beforehand through [[data understanding]].

Tasks involved:
1. **Data Integration**: Combining data from different sources, which can often generate missing data.
2. **Data Selection**: Deciding which data stays and which data is excluded.
3. **Data Quality Verification**: Identifying and addressing variables with missing data.
4. **Data Construction and Feature Engineering**: Creating new variables and features based on the existing data.

### [[data deployment]]

Need documents from [[data understanding]] and [[Obsidian-Integration-main/Data Preparation]] to give context ad deployment may be significantly after these.

Discoveries need to be recorded.
Data sources tracked, and imputation methods tracked, similar for features created.


### [[Missing Data]]

Example: KDD Cup 1998 Data on UCI ML Repo website

[[Data Dictionary]]: explaining the vars

Whats going on with the blanks?
What about lower rows?

census data: grouping/ data? Neibourhoods

Data explorer tools (javascipt) for each coloumn investigation
mean,vairence,skewness, min,max,sum, no.. zeros ect No. missings

When the number of missing repeats. 
Column names that look related.

Working theories we have.

Process to investigate: python
- row filter (focussing on a given filed)
- column filter
- number to string

### [[data explorer]]

What is the target varialbe

section up the data so not looking at all. Limit the number of variables.

Use a decision tree to investifate relationships between vars.

### [[imputation]]

How to do this properly?
Does it make sence to do 
Are there related vaiavbles? group bacsd on these

### [[standardised/KNIME]]

[[Obsidian-Integration-main/Data Preparation]]

[[Strategy for choosing Data Sources]]