# SQL Introduction

This repository contains SQL scripts for introductory exercises. Each script performs a specific task on a MySQL database.

## Requirements

- Scripts should end with a new line.
- SQL queries should have comments just before them.
- All files should start with a comment describing the task.
- SQL keywords should be in uppercase (SELECT, WHERE, etc.).

## File Descriptions

1. **0-list_databases.sql**: Lists all databases on the MySQL server.
2. **1-create_database_if_missing.sql**: Creates the database `hbtn_0c_0` if it doesn't exist.
3. **2-remove_database.sql**: Deletes the `hbtn_0c_0` database if it exists.
4. **3-list_tables.sql**: Lists all tables in a specified database.
5. **4-first_table.sql**: Creates a table called `first_table` in the `hbtn_0c_0` database.
6. **5-full_table.sql**: Prints the full description of the `first_table` in the `hbtn_0c_0` database.
7. **6-list_values.sql**: Lists all rows of the `first_table` in the `hbtn_0c_0` database.
8. **7-insert_value.sql**: Inserts a new row into the `first_table` in the `hbtn_0c_0` database.
9. **8-count_89.sql**: Counts the number of records with id = 89 in the `first_table` of the `hbtn_0c_0` database.
10. **9-full_creation.sql**: Creates the `second_table` in the `hbtn_0c_0` database and adds multiple rows.
11. **10-top_score.sql**: Lists all records of the `second_table` in the `hbtn_0c_0` database, ordered by score (top first).
12. **11-best_score.sql**: Lists all records with a score >= 10 in the `second_table` of the `hbtn_0c_0` database.
13. **12-no_cheating.sql**: Updates the score of Bob to 10 in the `second_table` without using Bob's id value.
14. **13-change_class.sql**: Removes all records with a score <= 5 in the `second_table` of the `hbtn_0c_0` database.
15. **14-average.sql**: Computes the score average of all records in the `second_table` of the `hbtn_0c_0` database.
16. **15-groups.sql**: Lists the number of records with the same score in the `second_table` of the `hbtn_0c_0` database.
17. **16-no_link.sql**: Lists all records of the `second_table` of the `hbtn_0c_0` database, filtering out rows without a name value, ordered by descending score.
18. **100-move_to_utf8.sql**: Converts the database `hbtn_0c_0`, the table `first_table`, and the field `name` in `first_table` to UTF8 (utf8mb4, collate utf8mb4_unicode_ci).
19. **101-avg_temperatures.sql**: Displays the average temperature (Fahrenheit) by city ordered by temperature (descending).
20. **102-top_city.sql**: Displays the top 3 of cities' temperature during July and August ordered by temperature (descending).
21. **103-max_state.sql**: Displays the max temperature of each state ordered by State name.

## Usage

To run any script, use the following command:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
