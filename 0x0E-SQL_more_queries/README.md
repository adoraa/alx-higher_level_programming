# SQL More Queries Project

This repository contains SQL scripts for various tasks related to database management. The scripts are designed to be executed on a MySQL server.

## Project Structure

- **Files**: SQL scripts for different tasks
  - `0-privileges.sql`: Script to create a MySQL user and manage privileges
  - `1-create_user.sql`: Script to create a MySQL server user with all privileges
  - `2-create_read_user.sql`: Script to create a database and a user with SELECT privilege
  - `3-force_name.sql`: Script to create a table with constraints
  - `4-never_empty.sql`: Script to create a table with a default value constraint
  - `5-unique_id.sql`: Script to create a table with a unique constraint
  - `6-states.sql`: Script to create a database and a table with a primary key constraint
  - `7-cities.sql`: Script to create a table with a foreign key constraint
  - `8-cities_of_california_subquery.sql`: Script to list cities from a specific state using subqueries
  - `9-cities_by_state_join.sql`: Script to list cities and their respective states using JOIN
  - `10-genre_id_by_show.sql`: Script to list shows and their genres
  - `11-genre_id_all_shows.sql`: Script to list shows and their genres, including NULL values
  - `12-no_genre.sql`: Script to list shows without a genre
  - `13-count_shows_by_genre.sql`: Script to count shows for each genre
  - `14-my_genres.sql`: Script to list genres of a specific show
  - `15-comedy_only.sql`: Script to list shows of a specific genre
  - `16-shows_by_genre.sql`: Script to list shows and their genres
  - `100-not_my_genres.sql`: Script to list genres not linked to a specific show
  - `101-not_a_comedy.sql`: Script to list shows without a specific genre
  - `102-rating_shows.sql`: Script to list shows by their rating
  - `103-rating_genres.sql`: Script to list genres by their rating sum

- **Database Dump**: Database dump file (`hbtn_0d_tvshows_rate.sql`) for testing purposes.

## Requirements

- MySQL 8.0
- Ubuntu 20.04 LTS
- Editor: vi, vim, emacs

## Usage

1. Clone the repository.
2. Import the database dump (`hbtn_0d_tvshows_rate.sql`) into your MySQL server.
3. Execute the SQL scripts using the `mysql` command with the appropriate arguments.
   Example: `cat 0-privileges.sql | mysql -hlocalhost -uroot -p`
4. Follow the instructions provided in each script's description.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
