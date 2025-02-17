### Many-to-Many Relationships

Occurs when multiple records in one table are associated with multiple records in another table.

Need to use a **junction table** (also known as a bridge table or associative entity). This table will contain foreign keys that reference the primary keys of the two tables involved in the relationship.

### Steps to Implement Many-to-Many Relationships

1. **Identify the Entities**: Determine the two entities that will participate in the many-to-many relationship. For example, consider `students` and `courses`.

2. **Create the Junction Table**: Create a new table that will serve as the junction table. This table will hold the foreign keys from both entities. In our example, we can create a table called `enrollments`.

3. **Define Foreign Keys**: In the junction table, define foreign keys that reference the primary keys of the two related tables. This establishes the relationship between the entities.

4. **Add Additional Attributes (if necessary)**: If needed, you can also include additional attributes in the junction table that are relevant to the relationship itself. For instance, you might want to track the enrollment date.

Example Schema

```sql
-- Create the students table
CREATE TABLE students (
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "email" TEXT UNIQUE NOT NULL
);

-- Create the courses table
CREATE TABLE courses (
    "id" INTEGER PRIMARY KEY,
    "title" TEXT NOT NULL,
    "description" TEXT
);

-- Create the junction table for the many-to-many relationship
CREATE TABLE enrollments (
    "student_id" INTEGER,
    "course_id" INTEGER,
    "enrollment_date" DATE NOT NULL,
    PRIMARY KEY("student_id", "course_id"), -- Composite primary key
    FOREIGN KEY("student_id") REFERENCES "students"("id"),
    FOREIGN KEY("course_id") REFERENCES "courses"("id")
);
```

A composite primary key (`student_id`, `course_id`) ensures that each student can enroll in a course only once.

To retrieve data from a many-to-many relationship, you can use SQL JOIN statements. For example, to find all courses a specific student is enrolled in, you can run:

```sql
SELECT courses.title
FROM courses
JOIN enrollments ON courses.id = enrollments.course_id
WHERE enrollments.student_id = 1;  -- Replace 1 with the desired student ID
```



[[Many-to-Many Relationships]]
   - Records in Table A relate to multiple records in Table B, and vice versa.
   - ==Requires a junction table== to manage the relationships.
   - Example: Students and Courses tables with a junction table Enrollments.