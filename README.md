# Virgil Full-stack Code Challenge

## Goal
The goal of this challenge is to help candidates to demonstrate their understanding of common practices in full-stack software development.

## What are we looking for?
- Candidate's ability to handle basic dev environment tools
- Candidate's ability to write React based UI Application
- Candidate's ability to design Restful API
- Candidate's ability to handle data manipulation

## Challenge
Write an application with a UI (React) and Back-end(Flask).
This app should display a list of **Account**
Each **Account** contains two types of **Credits**, **TypeA** and **TypeB**

- Client can create an Account
- Client can delete an Account
- Client can deposit an amount of any type of credits into an Account.
- Client can withdraw an amount of any type of credit from Account
- Client can set credit value of any type of credit an account
- Each of the above action should result in a transaction history being created
- Credits should not have negative value, attempts to withdraw more than the account has should result in error messages showing up
- Clients should be able to view transaction histories of an **Account**
*( feel free to either paginate the result or use infinite scroll )*

**NOTE:** Client here means a physical user, you should not worry about Authentication/Authorisation or User Model, any one has access to this application should have access to all features mentioned above.

**Additional Requirement:** Please manually add a delay/timeout(1 second) to the deposit/withdraw/set logic in the back-end.


## Technology choices
### Front-end
In the **transaction_history_ui** directory, a react-redux based template app is in place for you.
Redux and Redux-saga are not mandatory, feel free to use a  purely hook-based solution.
Feel free to pull in any libraries to achieve your Goal.
For Styling, please stick with CSS module for simplicity.

### Back-end
In the **transaction_history_backend** directory a Flask Hello-world app is setup for you.
Please feel free to use the framework of your choice to make the back-end.
Please manage your Python packages with Pipenv.
Feel free to pull in additional libraries to help you finish the challenge.

### Database
Please use SQL or NoSQL databases to help you finish this challenge

### Docker
Please write a docker-compose file, and a Dockerfile for each app.


## Deliverable
- Candidate should create a repository on github containing both services.
- Some seed data should be populated
- **docker-compose up** should be sufficient to spin up the stack
- Web interface should be accessible at localhost:3000
