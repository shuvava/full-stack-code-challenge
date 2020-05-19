# Virgil Full-stack Code Challenge


## Goal
The goal of this challenge is for candidates to demonstrate their understanding of common practices in full-stack software development.


## What are we looking for?
- Ability to handle basic dev environment tools
- Ability to write React based UI Application
- Ability to design Restful API
- Ability to handle data manipulation


## Time limit
There is no strict time limit on the challenge, but the recommended completion time is 4 to 8 hours.
Don't worry if you can not complete the entire end-to-end challenge.
We are more interested in your thinking process, design principles that you follow and the things that you worry about when you design the application.


## Challenge
Write an application with a UI (React) and Back-end (Flask).
This app should display a list of **Account**
This application should have two major components
- **Account** (model is provided)
- **CreditPack** (model is provided)

An Account contains multiple credit-packs, each credit-pack has amount, credit_type and expiry.
Account balance is calculated by adding up all of the same-typed credit-packs' amount.

For example:
cp1 = {
  "id": "...",
  "account-id": "...",
  "credit-type": "promotional",
  "amount": 5,
  "expiry": 2020-05-25
}
cp2 = {
  "id": "...",
  "account-id": "...",
  "credit-type": "promotional",
  "amount": 7,
  "expiry": 2020-08-25
}
cp3 = {
  "id": "...",
  "account-id": "...",
  "credit-type": "regular",
  "amount": 30,
  "expiry": 2021-01-25
}

Let cp1,cp2,cp3 be packs under account1. Then account should serialize to:
{
  "id": "...",
  "balance": {
    "promotional": 12,
    "regular": 30
  }
}

Backend:
- Client can create an Account
- Client can create many CreditPack under an Account
- Each CreditPack's creditType should be one of "promotional" and "regular"
- Promotional CreditPack should expire in 30 days
- Regular CreditPack should expire in 300 days
- Client can consume 1 credit at a time, system should consume creditPack that's closest to expiry date.

UI:
- Create a view with a list of Accounts. Feel free to not do pagination by just throwing in a big per_page parameter.
- In the above view, create an input field for account creation and a submit button, the only field we need is orgunit_id. (you don't have to worry about duplicated orgunit_id)
- Create an Account details view.
- In this details view, there should be a button on which the client can click to consume 1 credit from this account.
- In this details view, display a list of all creditPacks under this account
- In this details view, provide a form which the client can use to create new creditPacks
- In this details view, credit_packs should refresh whenever the user consumes a credit or posts a new creditPack


**NOTE:**
- Client here means a physical user, so do not worry about Authentication/Authorization or a User Model; any one who has access to this application should have access to all features mentioned above.
- Bonus points for adding test coverage to demonstrate different kind of test cases (e.g., TDD or BDD); however, test coverage is not the main concern of this challenge.

## Technology choices
### Front-end
In the **account_credit_ui** directory, a react-redux based template app is in place for you.
Redux and Redux-saga are not mandatory, feel free to use a pure hook-based solution if you prefer not use Redux and Redux-saga.
Feel free to pull in any libraries to help you achieve your Goal.
There is no restriction on the tool that you use to do styling.

### Back-end
In the **account_credit_backend** directory a Flask based app is setup for you.
- flask-sqlalchemy, psycopg2 and flask-migrate are in place for migrations.
- marshmallow is introduced for serialization
Feel free to swap out any of the technologies for your choice of libs.


### Docker
Please try to finish the docker-compose file to interconnect all services if you have time. (OPTIONAL)


## Deliverable
- Create a repository on github containing both services.
- **docker-compose up** to spin up the stack (OPTIONAL)
- Web interface should be accessible at localhost:3000 (OPTIONAL)


## To Run migrations
- run `docker-compose up` to bring up the postgres database container
- change directory to account_credit_backend folder
- run `pipenv install`
- run `pipenv shell`
- run `FLASK_APP=migrate.py:app flask db upgrade`

## To Run backend service
- change directory to account_credit_backend folder
- run `pipenv install`
- run `pipenv shell`
- run `python server.py`
