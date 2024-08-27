from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Date, ForeignKey, TIMESTAMP

# Create an engine to the SQLite database
engine = create_engine('sqlite:///real_estate_data.db', echo=True)

# Initialize metadata
meta = MetaData()

# Define tables based on the ERD

# Agents Table
agents = Table(
    'agents', meta,
    Column('agent_id', Integer, primary_key=True),
    Column('name', String),
    Column('assigned_properties', String),
    Column('experience_years', Integer),
    Column('average_rating', Float)
)

# Properties Table
properties = Table(
    'properties', meta,
    Column('property_id', Integer, primary_key=True),
    Column('property_name', String),
    Column('property_type', String),
    Column('price', Float),
    Column('size_sqft', Float),
    Column('bedrooms', Integer),
    Column('bathrooms', Integer),
    Column('developer_id', Integer),
    Column('property_tags', String)
)

# Users Table
users = Table(
    'users', meta,
    Column('user_id', Integer, primary_key=True),
    Column('name', String),
    Column('email', String),
    Column('phone', String),
    Column('age', Integer),
    Column('gender', String),
    Column('location', String),
    Column('income_level', String),
    Column('family_status', String)
)

# Sales Table
sales = Table(
    'sales', meta,
    Column('sale_id', Integer, primary_key=True),
    Column('property_id', Integer, ForeignKey('properties.property_id')),
    Column('buyer_id', Integer, ForeignKey('users.user_id')),
    Column('agent_id', Integer, ForeignKey('agents.agent_id')),
    Column('sale_price', Float),
    Column('sale_date', Date)
)

# Inspections Table
inspections = Table(
    'inspections', meta,
    Column('inspection_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('property_id', Integer, ForeignKey('properties.property_id')),
    Column('inspection_date', Date),
    Column('inspection_feedback', String)
)

# Interactions Table
interactions = Table(
    'interactions', meta,
    Column('interaction_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('property_id', Integer, ForeignKey('properties.property_id')),
    Column('interaction_type', String),
    Column('interaction_time', TIMESTAMP)
)

# Leads Table
leads = Table(
    'leads', meta,
    Column('lead_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.user_id')),
    Column('lead_score', Float),
    Column('lead_status', String)
)

# Create all tables in the database
meta.create_all(engine)

print("Database schema created successfully!")
