-- Question: What is the command to run a docker container, running PostgreSQL for a database called itam_db. I would like to specify the password for this database.
-- Answer: docker run --name itam_db -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres



-- create a schema called itam
create schema itam;

-- create two users called itam_user and itam_admin. itam_user should be able to read from and write to the tables in the itam schema. itam_admin should be able to read from and write to the tables in the itam schema and create and drop tables in the itam schema.
create user itam_user with password 'itam_user';
create user itam_admin with password 'itam_admin';
grant usage on schema itam to itam_user;
grant usage on schema itam to itam_admin;
grant select, insert, update, delete on all tables in schema itam to itam_user;
grant select, insert, update, delete on all tables in schema itam to itam_admin;
grant create on schema itam to itam_admin;
grant USAGE, create on schema itam to itam_admin;

-- grant ownership of the itam schema to itam_admin
alter schema itam owner to itam_admin;

-- create a table called depreciation_strategy in the itam schema. the table should have the following columns: id (int), name (varchar), description (varchar). the table should have a primary key on id.
-- id needs to be in quotes because it is a reserved word in postgresql
-- there are two values for depreciation_strategy: straight line and double declining balance
create table itam.depreciation_strategy (
    "id" int primary key,
    "name" varchar,
    "description" varchar
);

-- create a sequence called depreciation_strategy_seq, which should start at 1 and increment by 1 and should be used as the primary key for the depreciation_strategy table.
create sequence itam.depreciation_strategy_seq start 1 increment 1;

-- question: how do I make the sequence the primary key for the depreciation_strategy table?
-- answer: use the following command
alter table itam.depreciation_strategy alter column "id" set default nextval('itam.depreciation_strategy_seq'::regclass);

insert into depreciation_strategy (id, name, description) values (1, 'straight line', 'straight line');
insert into depreciation_strategy (id, name, description) values (2, 'double declining balance', 'double declining balance');

-- create a table called funding_details in the itam schema. the table should have the following columns: id (int), name (varchar),depreciation_strategy_id (int) and depreciation_rate (float). the table should have a primary key on id.
-- depreciation_stategy_id is a foreign key to the depreciation_strategy table.
-- id needs to be in quotes because it is a reserved word in postgresql
create table itam.funding_details (
    "id" int primary key,
    "name" varchar,
    "depreciation_strategy_id" int,
    "depreciation_rate" float
);

-- create a sequence called funding_details_seq, which should start at 1 and increment by 1 and should be used as the primary key for the funding_details table.
create sequence itam.funding_details_seq start 1 increment 1;

-- question: how do I make the sequence the primary key for the funding_details table?
-- answer: use the following command
alter table itam.funding_details alter column "id" set default nextval('itam.funding_details_seq'::regclass);

-- create a table called assets in the itam schema. the table should have the following columns: 
-- id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (int), salvage_value (float), purchase_date (date), funding_details_id (int). The table should have a primary key on id and a foreign key on funding_details_id.
-- id needs to be in quotes because it is a reserved word in postgresql
-- the table should have a sequence called assets_id_seq, which should start at 1 and increment by 1 and should be used as the primary key for the assets table.
create table itam.assets (
    "id" int primary key,
    "name" varchar,
    "status" varchar,
    "category" varchar,
    "cost" float,
    "useful_life" int,
    "salvage_value" float,
    "purchase_date" date,
    "funding_details_id" int
);

-- create a sequence called assets_seq, which should start at 1 and increment by 1 and should be used as the primary key for the assets table.
create sequence itam.assets_seq start 1 increment 1;

-- question: how do I make the sequence the primary key for the funding_details table?
-- answer: use the following command
alter table itam.assets alter column "id" set default nextval('itam.assets_seq'::regclass);

-- Generate a dataset of assets for an ITAM system. The dataset should include the following columns: id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (int), salvage_value (float), purchase_date (date), funding_details_id (int). The dataset should have 1000 rows, sorted by id. Each row should have the following characteristics:
-- - id should be a unique integer and sequential starting at 1.
-- - name should be a random string of characters between 1 and 50 characters long.
-- - status should be a random selection from the following valid asset statuses: in use, in storage, disposed of, in repair, in transit, other.
-- - category should be a random selection from the following valid categories: hardware, software, other.
-- - cost should be a random float between 0 and 100000.
-- - useful_life should be a random int between 1 and 10.
-- - salvage_value should be a random float greater than 0 but less than the cost of the asset.
-- - purchase_date should be a random date between 1/1/2019 and 12/31/2022.
-- - funding_details_id should be a random integer either 1 or 2.
-- The dataset should be saved as a CSV file named assets.csv in the data directory. The file should have a header row and the columns should have the following data types: id (int), name (varchar), status (varchar), category (varchar), cost (float), useful_life (float), salvage_value (float), funding_details_id (int)
insert into itam.assets (id, name, status, category, cost, useful_life, salvage_value, purchase_date, funding_details_id)
select
    id,
    name,
    status,
    category,
    cost,
    useful_life,
    salvage_value,
    purchase_date,
    funding_details_id
from (
    select
        row_number() over (order by random()) as id,
        md5(random()::text) as name,
        case
            when random() < 0.2 then 'in use'
            when random() < 0.4 then 'in storage'
            when random() < 0.6 then 'disposed of'
            when random() < 0.8 then 'in repair'
            when random() < 0.9 then 'in transit'
            else 'other'
        end as status,
        case
            when random() < 0.5 then 'hardware'
            when random() < 0.9 then 'software'
            else 'other'
        end as category,
        random() * 100000 as cost,
        (random() * 100)::int as useful_life,
        random() * (random() * 100000) as salvage_value,
        -- generate a random date between 1/1/2019 and 12/31/2022
        -- this does not work please fix
        -- '2019-01-01'::date + random() * ('2022-12-31'::date - '2019-01-01'::date) as purchase_date,
        '2019-01-01'::date + (random() * (DATE '2022-12-31' - DATE '2019-01-01')::integer)::integer as purchase_date
        case
            when random() < 0.5 then 1
            else 2
        end as funding_details_id
    from generate_series(1, 1000)
) as assets;


-- Generate a dataset of funding details for an ITAM system. The dataset should include the following columns: id (int), name (varchar), depreciation_strategy_id (int), depreciation_rate (float). The dataset should have 1000 rows, sorted by id. 
-- Each row should have the following characteristics:
-- - id should be a unique integer and sequential starting at 1.
-- - name should be a random string of characters between 1 and 10 characters long.
-- - depreciation_strategy_id should be a random integer either 1 or 2.
-- - depreciation_rate should be a random float between 0 and .4.

insert into itam.funding_details (id, name, depreciation_strategy_id, depreciation_rate)
select
    id,
    name,
    depreciation_strategy_id,
    depreciation_rate
from (
    select
        row_number() over (order by random()) as id,
        md5(random()::text) as name,
        case
            when random() < 0.5 then 1
            else 2
        end as depreciation_strategy_id,
        random() * 0.4 as depreciation_rate
    from generate_series(1, 1000)
) as funding_details;



CREATE TABLE itam.asset_locations (
    id SERIAL PRIMARY KEY,
    asset_id INTEGER NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES itam.assets (id)
);

grant select, insert, update, delete on all tables in schema itam to itam_user;
grant select, insert, update, delete on all tables in schema itam to itam_admin;
grant create on schema itam to itam_admin;
grant USAGE, create on schema itam to itam_admin;