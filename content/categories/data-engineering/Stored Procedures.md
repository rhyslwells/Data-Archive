---
aliases:
- null
category: CS
date modified: 27-09-2025
tags:
- algorithm
- database
---
Stored procedures are a way to automate SQL statements, allowing them to be executed repeatedly without rewriting the code.

**Demonstration with the Boston MFA Database**  

We will use the Boston MFA database to illustrate stored procedures. Previously, we implemented a soft-delete feature for the `collections` table using views. Now, we will create a stored procedure to achieve similar functionality.

1. **Select the Database**:
   ```sql
   USE `mfa`;
   ```

2. **Add a Deleted Column**:  
   The `deleted` column needs to be added to the `collections` table to track soft deletions.
   ```sql
   ALTER TABLE `collections` 
   ADD COLUMN `deleted` TINYINT DEFAULT 0;
   ```
   The `TINYINT` type is appropriate since the column will only hold values of 0 or 1, with a default of 0 to retain all existing collections.

3. **Change the Delimiter**:  
   Before creating a stored procedure, change the delimiter to allow multiple statements.
   ```sql
   delimiter //
   ```

4. **Create the Stored Procedure**:  
   Define the stored procedure to select current collections that are not marked as deleted.
   ```sql
   CREATE PROCEDURE `current_collection`()
   BEGIN
       SELECT `title`, `accession_number`, `acquired` 
       FROM `collections` 
       WHERE `deleted` = 0;
   END//
   ```

5. **Reset the Delimiter**:  
   After creating the procedure, reset the delimiter back to the default.
   ```sql
   delimiter ;
   ```

6. **Call the Stored Procedure**:  
   Execute the procedure to see the current collections.
   ```sql
   CALL current_collection();
   ```

7. **Soft Delete an Item**:  
   If we soft-delete an item, such as “Farmers working at dawn,” and call the procedure again, the deleted row will not appear in the output.
   ```sql
   UPDATE `collections` 
   SET `deleted` = 1 
   WHERE `title` = 'Farmers working at dawn';
   ```

### Parameters in Stored Procedures

Stored procedures can accept parameters. For example, we can create a procedure to handle the sale of artwork.

1. **Create the [[Transaction|Transactions]] Table**:
   ```sql
   CREATE TABLE `transactions` (
       `id` INT AUTO_INCREMENT,
       `title` VARCHAR(64) NOT NULL,
       `action` ENUM('bought', 'sold') NOT NULL,
       PRIMARY KEY(`id`)
   );
   ```

2. **Create the Sell Procedure**:  
   This procedure updates the `collections` table and logs the transaction.
   ```sql
   delimiter //
   CREATE PROCEDURE `sell`(IN `sold_id` INT)
   BEGIN
       UPDATE `collections` SET `deleted` = 1 
       WHERE `id` = `sold_id`;
       INSERT INTO `transactions` (`title`, `action`)
       VALUES ((SELECT `title` FROM `collections` WHERE `id` = `sold_id`), 'sold');
   END//
   delimiter ;
   ```

3. **Call the Sell Procedure**:  
   To sell a specific item, call the procedure with the item's ID.
   ```sql
   CALL `sell`(2);
   ```

### Considerations

- **Multiple Calls**:  
  If the `sell` procedure is called with the same ID multiple times, it may lead to multiple entries in the `transactions` table. Logic can be added to prevent this.

- **Programming Constructs**:  
  Stored procedures can be enhanced with programming constructs available in MySQL, allowing for more complex logic.
