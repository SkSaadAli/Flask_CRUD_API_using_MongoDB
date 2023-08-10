
# Flask Application for CRUD Operations on MongoDB

This repository contains a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API.

## Prerequisites

1. **Docker Desktop**: You must have Docker Desktop installed and configured on your system.

## Getting Started

1. **Clone the Repository**:
   
   ```sh
   git clone https://github.com/SkSaadAli/flask-api-task.git
   ```
   
2. **Navigate to the App Directory**:
   
   ```sh
   cd flask-api-task/app
   ```
   
3. **Pull MongoDB Image**:
   
   To set up the MongoDB container, pull the `mongo:4.4.6` Docker image:
   
   ```sh
   docker pull mongo:4.4.6
   ```
   
4. **Run Docker Compose**:
   
   Run the Docker Compose file to create and start the Flask application and MongoDB containers:
   
   ```sh
   docker-compose up
   ```
   
5. **Access the Local Server**:
   
   Open your web browser and navigate to `http://localhost:5000` to access the local server.

## Optional: Testing

For testing the CRUD operations, you can import the `flask-api-testing.json` collection into Postman. This collection contains tests for each CRUD operation of the server. To use it:

1. Import the collection into Postman.
2. Run the tests in the collection to verify the functionality of the CRUD operations.

## Conclusion

With these steps, you'll have a local Flask server set up for performing CRUD operations on a MongoDB database using a REST API.

### App Preview :

</table>
<table width="100%">
<tr>
<td width="100%">
<br>
<p align="center">
  Application At First Glance
</p>
<img src="https://raw.github.com/SkSaadAli/flask-api-task/main/ScreenShots%20and%20Testing%20Video/All_users.PNG?sanitize=true" >  
</td>
</table>

</table>
<table width="100%">
<tr>
<td width="100%">
<br>
<p align="center">
  Getting Single user with user_id
</p>
<img src="https://raw.github.com/SkSaadAli/flask-api-task/main/ScreenShots%20and%20Testing%20Video/Single_user_with_user_id.PNG?sanitize=true" >  
</td>
</table>

### Testing the API:
<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>

<img src="https://raw.github.com/SkSaadAli/flask-api-task/main/ScreenShots%20and%20Testing%20Video/all_api_tests.PNG?sanitize=true" >
</td> 
<td width="50%">
<br>

<img src="https://raw.github.com/SkSaadAli/flask-api-task/main/ScreenShots%20and%20Testing%20Video/all_test_passed.PNG?sanitize=true" >  
</td>
