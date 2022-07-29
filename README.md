# Tailor-API

## ABOUT

This is a web service which serves as an e-commerce platform specifically for tailors to host 
their shops online. It will serve as a one-stop-end where visitors can create and have their
Dresses sewn for them with minimal stress and maximum convenience.

## BASIC FUNCTIONALITY

A landing page with a list of available shops: 

 . visitors can:
 
    - View all approved shops on the page
    - View details of a particular/ preferred shop
    - Create an account
    
 . account owners can:
 
    - create shops to be added as part of listed shops
    - edit and update shop information
    
 . each shop must be approved by admin before listed as part of approved shops

### To run program:
Make sure you have Docker and docker-compose plugin installed on your machine.

1. Clone the repository:
```
  git clone <repository url>
```
2. Create a .env file in the project root directory and define:
```
SECRET_KEY, POSTGRES-credentials
```
3. Build the tailor app image from the Dockerfile and install dependencies, run the command;
  ```
  docker-compose build
  ```
  
4. Run the application in containers from the specified .yml file,
 ```
  docker-compose up
```

5. To run django management commands: run the command:
```
docker exec -it tailor_container /bin/bash/
```
