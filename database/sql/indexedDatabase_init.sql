-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;

-- Define ENUM types
CREATE TYPE EventTypeEnum AS ENUM (
    'Hackathon',
    'Concert',
    'Sports',
    'Conference',
    'Theatre',
    'Workshop',
    'Festival',
    'Webinar',
    'Exhibition',
    'Meetup',
    'Networking',
    'Seminar',
    'Tournament',
    'Charity',
    'Comedy',
    'Dance',
    'Other'
);

CREATE TYPE RegistrationStatusEnum AS ENUM (
    'Confirmed',
    'Pending',
    'Cancelled',
    'Waitlisted',
    'CheckedIn',
    'NoShow',
    'Declined',
    'Refunded',
    'Transferred'
);

-- Address table
CREATE TABLE Address (
    AddressID SERIAL PRIMARY KEY,
    ZipCode VARCHAR(20),
    City VARCHAR(100),
    Country VARCHAR(100),
    Location GEOGRAPHY(POINT, 4326)
);

-- Users table
CREATE TABLE Users (
    UserID SERIAL PRIMARY KEY,
    First VARCHAR(255) NOT NULL,
    Last VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(30),
    AddressID INT NOT NULL,
    CONSTRAINT FK_User_Address FOREIGN KEY (AddressID) REFERENCES Address(AddressID)
);

-- Organizers table
CREATE TABLE Organizers (
    OrganizerID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Contact VARCHAR(100),
    Rating INT CHECK (Rating >= 0 AND Rating <= 10)
);

-- Events table
CREATE TABLE Events (
    EventID SERIAL PRIMARY KEY,
    Title VARCHAR(255) NOT NULL,
    Description TEXT,
    EventType EventTypeEnum NOT NULL,
    Capacity INT CHECK (Capacity >= 0),
    Date DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME,
    AddressID INT NOT NULL,
    Price NUMERIC(10,2) CHECK (Price >= 0),
    FOREIGN KEY (AddressID) REFERENCES Address(AddressID)
);

-- EventOrganizators table
CREATE TABLE EventOrganizators (
    EventID INT NOT NULL,
    OrganizerID INT NOT NULL,
    PRIMARY KEY (EventID, OrganizerID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (OrganizerID) REFERENCES Organizers(OrganizerID)
);

-- Categories table
CREATE TABLE Categories (
    CategoryID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL UNIQUE
);

-- Services table
CREATE TABLE Services (
    ServiceID SERIAL PRIMARY KEY,
    ServiceType VARCHAR(100) NOT NULL UNIQUE
);

-- EventCategories table
CREATE TABLE EventCategories (
    EventID INT NOT NULL,
    CategoryID INT NOT NULL,
    PRIMARY KEY (EventID, CategoryID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);

-- EventServices table
CREATE TABLE EventServices (
    EventID INT NOT NULL,
    ServiceID INT NOT NULL,
    PRIMARY KEY (EventID, ServiceID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID)
);

-- Announcements table
CREATE TABLE Announcements (
    AnnouncementID SERIAL PRIMARY KEY, 
    Content TEXT NOT NULL, 
    Date DATE NOT NULL,
    EventID INT NOT NULL,
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Reviews table
CREATE TABLE Reviews (
    UserID INT NOT NULL,
    EventID INT NOT NULL,
    Rating INT CHECK (Rating >= 0 AND Rating <= 10),  
    Comment TEXT,             
    Date DATE,
    PRIMARY KEY (UserID, EventID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Registrations table
CREATE TABLE Registrations (
    UserID INT NOT NULL,
    EventID INT NOT NULL,
    Status RegistrationStatusEnum,
    Ticket VARCHAR(100),
    Date DATE,
    PRIMARY KEY (UserID, EventID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

-- Indexes for performance optimization

-- Events table indexes
CREATE INDEX idx_events_date ON Events(Date);
CREATE INDEX idx_events_addressid ON Events(AddressID);

-- Address table indexes
CREATE INDEX idx_address_city_id ON Address(City, AddressID);

-- Organizers table indexes
CREATE INDEX idx_organizers_name ON Organizers(Name);

-- Categories table indexes
CREATE INDEX idx_categories_name ON Categories(Name);

-- Reviews table indexes
CREATE INDEX idx_reviews_eventid_rating ON Reviews(EventID, Rating);

-- Registrations table indexes
CREATE INDEX idx_registrations_userid ON Registrations(UserID);