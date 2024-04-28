## 0x0F. Python - Object-relational mapping

### Object Relational Mapping - SQLAlchemy

This project contains scripts written in Python using SQLAlchemy, an Object Relational Mapper (ORM) for working with SQL databases. Each script performs different tasks related to database management, querying, and relationships between tables.

### Files

- **0-select_state.py**: Script to list all states from the database.
- **1-filter_states.py**: Script to list all states starting with 'N' from the database.
- **2-my_filter_states.py**: Script to take in an argument and display all values in the states table of hbtn_0e_0_usa where name matches the argument.
- **3-my_safe_filter_states.py**: Script to take in an argument and display all values in the states table of hbtn_0e_0_usa where name matches the argument. This script is safe from MySQL injection.
- **4-cities_by_state.py**: Script to list all cities from the database hbtn_0e_4_usa.
- **5-filter_cities.py**: Script to take in the name of a state as an argument and list all cities of that state.
- **6-model_state.py**: Script that contains the class definition of a State and an instance Base = declarative_base().
- **7-model_state_fetch_all.py**: Script to list all State objects from the database hbtn_0e_6_usa.
- **8-model_state_fetch_first.py**: Script to print the first State object from the database hbtn_0e_6_usa.
- **9-model_state_filter_a.py**: Script to list all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
- **10-model_state_my_get.py**: Script to print the State object with the name passed as an argument from the database hbtn_0e_6_usa.
- **11-model_state_insert.py**: Script to add the State object “Louisiana” to the database hbtn_0e_6_usa.
- **12-model_state_update_id_2.py**: Script to change the name of a State object from the database hbtn_0e_6_usa.
- **13-model_state_delete_a.py**: Script to delete all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
- **model_city.py**: Contains the class definition of a City.
- **relationship_city.py**: Contains the class definition of a City with relationship to State.
- **relationship_state.py**: Contains the class definition of a State with relationship to City.
- **100-relationship_states_cities.py**: Script to create the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa.
- **101-relationship_states_cities_list.py**: Script to list all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa.
- **102-relationship_cities_states_list.py**: Script to list all City objects from the database hbtn_0e_101_usa, including their corresponding State objects.
