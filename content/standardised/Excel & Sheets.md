---
title: 
tags:
  - software
  - business
aliases: 
category:
---
##### Links

[Google sheets example folder](https://drive.google.com/drive/folders/1F9GTIK-MARSjl6-BKb1AOID6EoRLe_zk?usp=drive_link)

see [[standardised/GSheets|GSheets]]

Excel Example folder: Desktop/Example_Examples

## Tools common to Excel and Sheets

##### Vlookup

Table

| **Product ID** | **Product Name** | **Price** |
| -------------- | ---------------- | --------- |
| 1001           | Apple            | $1.00     |
| 1002           | Banana           | $0.50     |
| 1003           | Orange           | $0.80     |

$0.50=VLOOKUP(1002, Table, 3, FALSE)
##### Pivot table


## Excel specific

index-match

index-match-match
##### Excel: Evaluate Formula

**Evaluate Formula** is a feature in Excel that allows you to step through complex formulas to see how Excel calculates the result. This tool is helpful for debugging or understanding how nested formulas work.

**Example:**
Suppose you have a formula like this:
```excel
=IF(SUM(A1:A3) > 10, A4 * 2, A5 + 5)
```
To understand how Excel processes this formula, you can use **Evaluate Formula**. It will break down the formula into steps, showing how the `SUM(A1:A3)` is calculated, followed by the evaluation of the `IF` condition, and finally either the multiplication or addition operation based on the result.

**How to use it:**
1. Select the cell containing the formula.
2. Go to the "Formulas" tab on the ribbon.
3. Click on "Evaluate Formula".
4. Click "Evaluate" to step through each part of the formula.

##### Excel: What-If Analysis

**What-If Analysis** in Excel allows you to explore different scenarios by changing the inputs to your formulas. The three main tools within What-If Analysis are **Scenario Manager**, **Goal Seek**, and **Data Tables**.

- **Scenario Manager**: Lets you save different sets of input values and switch between them to see the impact on the result.
- **Goal Seek**: Finds the required input value to achieve a specific output.
- **Data Tables**: Shows how changing one or two variables affects your formulas.

**Example (Goal Seek):**
Imagine you have a loan payment formula:
```excel
=PMT(interest_rate, number_of_periods, loan_amount)
```
You want to find out what interest rate would result in a monthly payment of $500.

Steps:
1. Enter the formula with an initial guess for the interest rate.
2. Go to "Data" > "What-If Analysis" > "Goal Seek".
3. Set the cell with the formula to a value of 500.
4. Set the interest rate cell as the one to change.
5. Click "OK" and Excel will adjust the interest rate to meet the target.

##### Excel: Forecast Sheets

**Forecast Sheets** use historical data to predict future values. Excel creates a forecast chart based on the pattern in the data, using linear or exponential smoothing models. This is particularly useful for time series data, such as sales or financial data over time.

**Example:**
Suppose you have monthly sales data in a column:

| Month  | Sales |
|--------|-------|
| Jan    | 1000  |
| Feb    | 1100  |
| Mar    | 1200  |
| Apr    | 1300  |
You want to forecast future sales for the next 6 months.

Steps:
1. Select the range of historical data (both months and sales).
2. Go to the "Data" tab on the ribbon.
3. Click "Forecast Sheet".
4. Excel will automatically create a forecast for the future months based on the trend in the data.
5. You can adjust the forecast options (e.g., forecast length, confidence intervals) before creating the sheet.
##### Excel: Consolidate

In Excel, the **Consolidate** feature (found under the **Data** tab) allows you to combine data from multiple ranges or worksheets into a single summary. It is particularly useful when you have data spread across different locations and want to summarize it, such as calculating totals, averages, or other aggregate functions.

Key Features of Consolidate:
- **Multiple Ranges**: You can consolidate data from different ranges, even if they are in separate worksheets or workbooks.
- **Functions**: It provides several functions such as SUM, AVERAGE, COUNT, MIN, MAX, and more to aggregate the data.
- **Labels**: You can use row and column labels to match and consolidate the data correctly.

How to Use Consolidate:
1. **Prepare your data**: Ensure that your data is organized in a table format with similar structures (e.g., same columns and rows across different sheets or ranges).
2. **Navigate to Consolidate**: Go to the **Data** tab and click on **Consolidate** in the **Data Tools** group.
3. **Select Function**: In the Consolidate dialog box, select the function you want to use (e.g., **Sum**, **Average**, etc.).
4. **Add References**: Add the ranges you want to consolidate by clicking on **Add** after selecting the range. You can select ranges from different worksheets or workbooks.
5. **Use Labels**: If your data contains row or column labels, check the boxes for "Use labels in top row" or "Use labels in left column" to consolidate the data correctly based on these labels.
6. **Create links**: If you want the consolidated data to update automatically when the source data changes, check the box for **Create links to source data**.

Benefits:
- Saves time by avoiding manual data entry or copy-pasting from multiple sheets.
- Helps in summarizing large amounts of data quickly.
- Ensures accuracy in consolidation, especially with functions like **Sum** or **Average**.

Example:
Suppose you have sales data in two worksheets as follows:

**Sheet1 (Region A)**:

| Product | Sales |
|---------|-------|
| A       | 100   |
| B       | 200   |
| C       | 300   |

**Sheet2 (Region B)**:

| Product | Sales |
|---------|-------|
| A       | 150   |
| B       | 250   |
| C       | 350   |
You can use the **Consolidate** feature to combine the sales from both regions into a summary table:

**Consolidated Sheet**:

| Product | Sales |
|---------|-------|
| A       | 250   |
| B       | 450   |
| C       | 650   |

In this case, you would use the **Sum** function in the Consolidate dialog to add the sales from the two regions.
##### Excel: Text to Columns

The **Text to Columns** feature in Excel is used to split the data in one column into multiple columns, based on a delimiter (like commas, spaces, or tabs) or a fixed width. This is particularly helpful when you have data combined in a single column and you need to separate it into distinct parts.

Benefits:
- Efficiently splits combined data without manual editing.
- Helps with data cleaning when importing text-based data from sources like CSV files.
- Reduces errors by automating the process of separating values.

Key Features of Text to Columns:
- **Delimiters**: You can split text based on specific delimiters such as commas, spaces, semicolons, or custom characters.
- **Fixed Width**: If the data is in a consistent format, you can split the text based on fixed-width segments.

How to Use Text to Columns:
1. **Select the Data**: Highlight the column or cells that contain the text you want to split.
2. **Navigate to Text to Columns**: Go to the **Data** tab on the ribbon, then click **Text to Columns** in the **Data Tools** group.
3. **Choose the Split Type**:
   - **Delimited**: Choose this option if your data is separated by characters like commas, tabs, or spaces.
   - **Fixed Width**: Choose this if the data is aligned into specific columns with consistent spacing.
4. **Select Delimiters or Set Width**: 
   - For **Delimited**, choose the character that separates your data (e.g., comma, space, semicolon).
   - For **Fixed Width**, manually set where the splits should occur by clicking in the preview window.
5. **Select Destination**: Choose where you want the split data to appear (by default, it will overwrite the original data).
6. **Finish**: Click **Finish** to apply the split.

Example 1: Delimited (Comma-Separated Values)
Imagine you have a list of full names in one column:

| Full Name        |
|------------------|
| John,Smith       |
| Jane,Doe         |
| Robert,Johnson   |

You want to split these names into two separate columns: First Name and Last Name. Here's how you would use **Text to Columns**:
1. Select the column with the full names.
2. Go to **Data** > **Text to Columns**.
3. Choose **Delimited**, then select **Comma** as the delimiter.
4. Click **Finish**. The data will be split into two columns:

| First Name | Last Name |
|------------|-----------|
| John       | Smith     |
| Jane       | Doe       |
| Robert     | Johnson   |

Example 2: Fixed Width
Suppose you have a column with product codes where each section of the code has a fixed length:

| Product Code   |
|----------------|
| 12345ABC67890  |
| 67890DEF12345  |

If the first 5 characters are the product number, the next 3 characters are the product category, and the last 5 characters are the batch number, you can split them based on fixed widths:
1. Select the column with the product codes.
2. Go to **Data** > **Text to Columns**.
3. Choose **Fixed Width**.
4. In the preview window, set the breaks where you want to split the text (after the 5th and 8th characters).
5. Click **Finish**. The data will be split into separate columns like this:

| Product Number | Category | Batch Number |
|----------------|----------|--------------|
| 12345          | ABC      | 67890        |
| 67890          | DEF      | 12345        |

##### Excel: [[Data Validation]]
- **Restrict Data Types**: You can limit entries to specific data types, such as whole numbers, decimal numbers, dates, or times.
- **Set Input Rules**: You can set conditions (e.g., numbers between 1 and 100, dates in a certain range, or specific text lengths).
- **Create Drop-Down Lists**: You can provide users with a predefined list of options to select from.
- **Custom Validation**: You can use formulas for advanced validation rules.
- **Error Alerts**: You can display custom messages to users when they try to enter invalid data.

How to Use Data Validation:

1. **Select the Cell(s)**: Select the range of cells where you want to apply data validation.
2. **Go to Data Validation**: Navigate to the **Data** tab on the ribbon, and in the **Data Tools** group, click **Data Validation**.
3. **Set Validation Criteria**:
   - In the **Settings** tab, choose the type of data you want to allow (Whole Number, Decimal, List, Date, Time, Text Length, or Custom).
   - Specify the condition (e.g., a range of values or a list of items).
4. **Input Message (Optional)**: In the **Input Message** tab, you can set a message that will appear when the user selects the cell, providing guidance on what they should enter.
5. **Error Alert**: In the **Error Alert** tab, define what happens if invalid data is entered. You can show an error message and choose whether to stop the entry, give a warning, or provide information.

**Restricting Input to a Range of Numbers**
You want to restrict the values in a certain column to only allow whole numbers between 10 and 100.
   
Steps:
1. Select the column or cells where you want to apply the rule.
2. Go to **Data** > **Data Validation**.
3. In the **Settings** tab, choose **Whole Number** from the **Allow** drop-down.
4. Set the **Minimum** to 10 and the **Maximum** to 100.
5. Optionally, create an input message or error alert to inform the user of the valid range.

**Creating a Drop-Down List**
You want users to select from a list of predefined options, such as product categories (e.g., "Electronics", "Furniture", "Clothing").
Steps:
1. Select the cells where the drop-down list should appear.
2. Go to **Data** > **Data Validation**.
3. In the **Settings** tab, choose **List** from the **Allow** drop-down.
4. In the **Source** field, type the list items, separated by commas: `Electronics,Furniture,Clothing`.
5. Click **OK**. Now users will see a drop-down arrow in the cells, allowing them to choose from the options.

**Validating Dates**
You want to ensure that users can only enter dates within a specific range, such as between January 1, 2023, and December 31, 2023.
Steps:
1. Select the cells where the dates will be entered.
2. Go to **Data** > **Data Validation**.
3. In the **Settings** tab, choose **Date** from the **Allow** drop-down.
4. Set the **Start Date** to 1/1/2023 and the **End Date** to 12/31/2023.
5. Click **OK**. Now users will only be able to enter dates within the specified range.

**Custom Validation with Formulas**
You want to ensure that users can only enter text starting with the letter "A".
Steps:
1. Select the cells where the validation should apply.
2. Go to **Data** > **Data Validation**.
3. In the **Settings** tab, choose **Custom** from the **Allow** drop-down.
4. In the **Formula** field, enter:
   ```excel
   =LEFT(A1, 1)="A"
   ```
5. Click **OK**. Now users will only be able to enter text starting with the letter "A".


## Google specific

Xlookup