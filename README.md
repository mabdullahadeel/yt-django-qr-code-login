# Discord Like QR Code Login

This repo holds the code for a demo app that shows how to use QR codes to login to a web app.

<hr>

## Important Links

- Youtube Tutorial -> https://youtu.be/8Pi5wp732Xw
- Medium Post -> https://medium.com/@abdadeel/how-to-add-discord-like-qr-code-login-d2cef2f5657f
- Architecture Diagram -> http://bit.ly/3IfywmD

<hr>

## Backend

### Tech Stack

- Django
- Django Rest Framework
- Django Channels
- Postgresql
- Redis

#### Prerequisites

- Python >=3.9

### How to run

- Clone the repo
- Move to the `backend` folder
  ```bash
   cd backend
  ```
- Create a virtual environment by running
  ```bash
  python -m venv env
  #OR
  python -m virtualenv env
  ```
- Activate the virtual environment

  ```bash
   # Linux or Mac
   source env/bin/activate

   # Windows
   env\Scripts\activate
  ```

- Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
- To setup the database, either use docker or install postgresql on your machine.
  - To use docker, run
    ```bash
    docker-compose -f local.yml up -d
    ```
  - To install postgresql on your machine, follow the instructions [here](https://www.postgresql.org/download/)
- Apply migrations
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- To run the backend server, run
  ```bash
  python manage.py runserver
  ```

<hr>

## Frontend

### Tech Stack

- React/Nextjs
- Typescript
- ChakraUI

#### Prerequisites

- Node >=16

### How to run

- Clone the repo
- Move to the `frontend` folder
  ```bash
   cd frontend
  ```
- Install dependencies

  ```bash
    npm install

    #Or

    yarn
  ```

- To run the frontend server, run

  ```bash
    npm run dev

    #Or

    yarn dev
  ```

- The frontend will start on https://localhost:3000
