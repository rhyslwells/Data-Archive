---
title: What is a Soft Delete?
tags:
  - data_integrity
  - data_management
---
**Soft deletion** is a technique used in databases to ==mark records as deleted without physically removing them from the database==. 

This approach is particularly useful in scenarios where [[data integrity]] and synchronization are important, such as during **[[Incremental Synchronization]]**.

When using [[incremental synchronization]] modes, fully deleted records from a source system are not replicated. To handle this, a field can be added to each record to indicate whether it should be treated as deleted. This allows the system to maintain a complete history of records while still functioning as if certain records are removed.

## Implementation

A common way to implement soft deletion is by adding a boolean flag, such as `is_deleted`, to the record [[Database Schema|schema]]. Here’s how it works:

1. **Flagging Records**:
   - When a record is "deleted," the `is_deleted` flag is set to `true`.
  
2. **Querying Data**:
   - All [[Querying|queries]] must be designed to exclude records where `is_deleted` is `true`. For example:
     ```sql
     SELECT * FROM table_name WHERE is_deleted = false;
     ```

3. **Background Jobs**:
   - Periodically, background jobs can be executed to permanently remove records marked as deleted, if necessary, or to archive them for future reference.

## Benefits

- **Data Integrity**: Maintains a complete history of records, which can be useful for auditing and recovery.
- **Ease of Recovery**: Records can be easily restored by simply resetting the `is_deleted` flag.
- **Synchronization**: Facilitates incremental synchronization by ensuring that deleted records are still present in the database.

## Considerations

- **Query Complexity**: Requires careful query design to ensure that deleted records are consistently excluded.
- **Storage**: Over time, soft-deleted records can accumulate, potentially leading to increased storage requirements.

## Example of Soft Deletion

Let's say we have a table named `users` that stores user information. We will add a boolean column called `is_deleted` to indicate whether a user is "deleted."

In this example, we demonstrated how to implement soft deletion using a boolean flag in the `users` table. This approach allows for easy recovery of deleted records and maintains [[data integrity]] while facilitating incremental synchronization.

#### Step 1: Modify the Table Structure

First, we need to alter the `users` table to add the `is_deleted` column:

```sql
ALTER TABLE users ADD COLUMN is_deleted BOOLEAN DEFAULT false;
```

#### Step 2: Soft Delete a User

When a user wants to delete their account, instead of removing the record from the database, we update the `is_deleted` flag:

```sql
UPDATE users SET is_deleted = true WHERE user_id = 123;
```

#### Step 3: Querying Active Users

To retrieve a list of active users (those who are not deleted), we write our queries to exclude soft-deleted records:

```sql
SELECT * FROM users WHERE is_deleted = false;
```

#### Step 4: Restoring a Soft Deleted User

If a user decides to restore their account, we can simply set the `is_deleted` flag back to `false`:

```sql
UPDATE users SET is_deleted = false WHERE user_id = 123;
```

#### Step 5: Permanently Deleting Soft Deleted Users

If we want to permanently remove users who have been soft deleted for a certain period, we can run a background job to delete those records:

```sql
DELETE FROM users WHERE is_deleted = true AND deletion_date < NOW() - INTERVAL '30 days';
```
