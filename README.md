# Virgil Full-stack Code Challenge

## Goal
The goal of this challenge is for candidates to demonstrate their understanding of common practices in full-stack software development.

## What are we looking for?
- Ability to handle basic dev environment tools
- Ability to write React based UI Application
- Ability to design Restful API
- Ability to handle data manipulation

## Challenge
Write an application with a UI (React) and Back-end (Flask).
This app should display a list of **Account**
Each **Account** contains two types of **Credits**, **TypeA** and **TypeB**

- Client can create an Account
- Client can delete an Account
- Client can deposit an amount to a credit type in an account
- Client can withdraw an amount from a credit type in an account
- Client can set credit value of a credit type in an account
- Each of the above actions should result in a transaction history being created
- Account should not have negative credit value. Attempts to withdraw more than the account has
or attempts to set the value of the account to negative value should result in error messages showing up
- Client can view transaction histories of an **Account**
*( feel free to either paginate the result or use infinite scroll )*

**NOTE:**
- Client here means a physical user, so do not worry about Authentication/Authorization or a User Model; any one who has access to this application should have access to all features mentioned above.
- Bonus points for adding test coverage to demonstrate different kind of test cases (e.g., TDD or BDD); however, test coverage is not the main concern of this challenge.

**Additional Requirement:** Please manually add delay/timeout (1 second) to deposit/withdraw/set logic in the back-end.


## Technology choices
### Front-end
In the **transaction_history_ui** directory, a react-redux based template app is in place for you.
Redux and Redux-saga are not mandatory, feel free to use a pure hook-based solution if you prefer not use Redux and Redux-saga.
Feel free to pull in any libraries to help you achieve your Goal.
For Styling, please stick to CSS module for simplicity.

### Back-end
In the **transaction_history_backend** directory a Flask Hello-world app is setup for you.
Please feel free to use the framework of your choice to make the back-end.
Please manage your Python packages with `pipenv`.
Feel free to pull in additional libraries to help you finish the challenge.

### Database
Please use SQL or NoSQL databases to help you finish this challenge

### Docker
Please write a docker-compose file, and a Dockerfile for each app.


## Deliverable
- Create a repository on github containing both services.
- Include seed data to populate the application.
- `docker-compose up` should be sufficient to spin up the stack
- Web interface should be accessible at localhost:3000
