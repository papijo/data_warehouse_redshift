# Data Warehousing Project with Amazon Redshift and S3

## Project description

The goal of the project is to build an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for analytics to be done on the project to find insights in what songs users are listening to.

## How to Run

To run this project, you will to create a configuration file with the following environment variables:

```
[CLUSTER]
HOST=''
DB_NAME=''
DB_USER=''
DB_PASSWORD=''
DB_PORT=5439

[IAM_ROLE]
ARN=

[S3]
LOG_DATA='s3://udacity-dend/log_data'
LOG_JSONPATH='s3://udacity-dend/log_json_path.json'
SONG_DATA='s3://udacity-dend/song_data'

[AWS]
KEY=
SECRET=

[DWH]
DWH_CLUSTER_TYPE       = multi-node
DWH_NUM_NODES          = 4
DWH_NODE_TYPE          = dc2.large
DWH_CLUSTER_IDENTIFIER =
DWH_DB                 =
DWH_DB_USER            =
DWH_DB_PASSWORD        =
DWH_PORT               = 5439
DWH_IAM_ROLE_NAME      =
```

## Table of Contents

- [Project Description](#project-description)
- [How to Run](#how-to-run)
- [Project Structure](#project-structure)
- [Database Schema Design](#database-schema-design)
  - [Staging Tables](#staging-tables)
  - [Fact Table](#fact-table)
  - [Dimension Tables](#dimension-tables)
- [Queries and Results](#queries-and-results)
- [Project Lifecycle](#project-lifecycle)

## Project Structure

This project includes 3 python scripts and a jupyter notebook.

- sql_queries.py script contains the sql queries for dropping tables, creating staging tables and inserting data from Amazon S3 storage to Amazon Redshift cluster.

- db_operations.py script contains the code for creating the analytics table and for inserting data from staging tables to the analytics table.

- analytics.py script contains the code to verify the data converted or loaded into the Redshift Analytics Table

-etl.py script contains the code to load the data from Amazon S3 to Redshift Staging tables and from the staging tables to the analytics tables making use of the db_operations script and the sql_queries script.

## Database schema design

### Staging Tables

- staging_events

### Fact Table

- songplays - records in event data associated with song plays i.e. records with page NextSong -
  _songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent_

### Dimension Tables

- users - users in the app -
  _user_id, first_name, last_name, gender, level_
- songs - songs in music database -
  _song_id, title, artist_id, year, duration_
- artists - artists in music database -
  _artist_id, name, location, lattitude, longitude_
- time - timestamps of records in songplays broken down into specific units -
  _start_time, hour, day, week, month, year, weekday_

## Queries and Results

Number of rows in each table:

| Table          |  rows |
| -------------- | ----: |
| staging_events |  8056 |
| staging_songs  | 14896 |
| artists        | 10025 |
| songplays      |   333 |
| songs          | 14896 |
| time           |  8023 |
| users          |   105 |

## Project Lifecyle

Connection to the Amazon Cluster is closed and the cursor deleted when the cluster resources are no longer needed.
