## Integrative Project  _UVM_

## Stage 1

This activity involves applying the knowledge acquired throughout the course and revisiting what was learned in previous subjects to integrate different disciplines. Additionally, it references previously developed activities to ensure the cross-curricular nature of the reviewed content, thus strengthening the development of competencies.

The project consists of installing the infrastructure of a distributed system under a client-server architecture. To clearly apply the concept of a distributed system, at least two computers connected in a network should be used.

The distributed system to be installed will consist of:

- Database server (Server equipment)
- Web server (Server equipment)
- Client (Client equipment)
- The objective of the first part of the Integrative Project is to install and configure the server equipment:

Database server
Web server
Process Explanation
Installation
Install and configure the database server of your choice on the server equipment. MySQL Server is suggested, which you can download from the following page: https://dev.mysql.com/downloads/

The database was created in Ubuntu.

Before installing any package, it is recommended to update the operating system.

During the installation, a password was requested.

The installation of MySQL in Ubuntu is relatively easy because the MySQL Server package is available in Ubuntu's official repositories. This simplifies the installation and software update process through the APT package management system.

Database Creation
Create a database for access control and insert data into it. Users must log in using a username and password, and each user must have an assigned role (Roles: Administrator, Operative, General).

The following link can support you: https://evilnapsis.com/2016/09/05/3-modelos-de-base-de-datos-para-tabla-de-usuarios/

First, we review the databases we currently have:

Create the Role table:

sql
'''
CREATE DATABASE ms_multi_users_db;
SHOW DATABASES;
USE ms_multi_users_db;

CREATE TABLE Rol (
RolId INT NOT NULL AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
created_at DATETIME,
PRIMARY KEY (RolId)
);

SHOW TABLES;

CREATE TABLE User (
UserId INT NOT NULL AUTO_INCREMENT,
name VARCHAR(20) NOT NULL,
password VARCHAR(50) NOT NULL,
RolId INT,
created_at DATETIME,
PRIMARY KEY (UserId),
FOREIGN KEY (RolId) REFERENCES Rol(RolId)
);

INSERT INTO Rol (name, created_at) VALUES ('Administrator', NOW());
INSERT INTO Rol (name, created_at) VALUES ('Operative', NOW());
INSERT INTO Rol (name, created_at) VALUES ('General', NOW());

INSERT INTO User (name, password, RolId, created_at) VALUES ('MatyAdmin', 'MatyAdmin', 1, NOW());
INSERT INTO User (name, password, RolId, created_at) VALUES ('MatyOperative', 'MatyOperative', 2, NOW());
INSERT INTO User (name, password, RolId, created_at) VALUES ('MatyGeneral', 'MatyGeneral', 3, NOW());

'''
Entity-relationship diagram of the database:

Conclusion
By installing and creating databases in MySQL on Ubuntu, I have gained knowledge on how to configure and manage a database environment, create data structures, and interact with data using basic SQL commands. These skills will allow me to start developing applications and systems that require data storage and manipulation.

##Stage 2
Objective
The objective of the second part of the Integrative Project is to establish the connection from a web application to the database and use the client equipment to visualize the application as a web client, thus completing the distributed system structure outlined in Stage 1 of your Integrative Project.

Instructions
Using your preferred development IDE (Suggested IDEs: Visual Studio, Eclipse, NetBeans), create a login web application with the following requirements:

Login screen:
User field (text box for input)
Password field (text box for input)
Role field (dropdown list with the defined roles)
The application must connect to the database created in Stage 1 of the integrative project (if necessary, make adjustments to your database) and perform the corresponding validations to log in.
Send corresponding error messages when the data is incorrect.
Access the developed web application from a browser on the Client equipment and perform the respective tests with your database data.

The deliverables that will form part of your work are the following:

Explanation of the process performed
Screenshots that demonstrate the development
Analysis of the developed distributed system
Distributed system architecture scheme. Include an explanation of the function of each element.
Development
We start with the installation of Flask and its requirements.

Install MySQL.

The next step is to create the code using Visual Studio Code with the Python language.

Indicate the requirements.

Create the login controllers.

Controllers for Flask.

Assign Ajax for login.

Assign User, password, and roles.

Create the web server:

Add the views for:

Home
Successful login screen:

Error login screen:

Login:

Login screen:

Login:

Login with the user and password assigned in the database:

Verify that it is correct and return to the home screen:

Attempt to log in with a user not existing in the database:

Receive an error and return to the home screen:

Verify that there are no errors made in the login process:

During the project, I had several errors like lazy load, which was running the cursor in the background because I had duplicated it at the beginning. Another error was callable, which was not executing the cursor. The definition of roles in table creation also had errors, as well as adding users.

The creation of the front-end was partly with the help of external pages as I am not very familiar with HTML.

Conclusion
The project was a challenge; I had knowledge of databases, which made the first part of the project easier, but the second part was more difficult because it was a long code where I had to link the database with the server so that the client has visibility. Using Flask and making the connections between MySQL and Python was quite a challenge. It is also essential to ensure that the user has the appropriate permissions to access the database and execute the necessary queries. It is important to carefully review and debug the code to identify and correct possible errors.

References
School W. (n.d.). W3 School. Retrieved from Python MySQL Create Database: https://www.w3schools.com/python/python_mysql_create_db.asp
Microsoft Azure (2017). Batch Processing. Retrieved from https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/batch-processing
Yuson P. (2017). Types of Mainframe Processing: Batch and Online. Retrieved from http://conceptsolutionsbc.com/wordpress/types-of-mainframe-processing-batch-and-online/
