# write the postgres command to load data into the database from a csv
# file named assets.csv in the data directory
# the file should have a header row and the columns should have the data types
# id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (float), salvage_value (float), funding_details (varchar), depreciation_strategy (varchar)
# the file should be loaded into a table named assets
# the table should be created if it does not exist
# the table should be truncated before loading the data

create table if not exists assets (
    id int,
    name varchar,
    status varchar,
    category varchar,
    cost float,
    useful_life float,
    salvage_value float,
    funding_details varchar,
    depreciation_strategy varchar
);

psql -d postgres -c "copy assets from '/data/assets.csv' delimiter ',' csv header;"