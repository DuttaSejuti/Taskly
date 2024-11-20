# Taskly 📔 
Taskly is a simple ToDo app built with FastAPI, VueJS, and PostgreSQL with Docker. User can create, update, delete, and search their tasks.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)


## Installation Guide
To run Taskly locally, follow the following instructions
1. ©️ **Clone the repository**
   ```bash
   git clone https://github.com/DuttaSejuti/Taskly.git
    ```
2. 🔅 **Navigate to the project directory**
    ```bash
    cd Taskly
    ```
3. 🔧 **Set up the Environment variables**

   Create a `.env` file in the root directory using the provided `.env_example` as a template, or just use the command. Change the variables according to your DB settings.
   ```bash
   cp .env_example .env
   ```
4. 🏃 **Build and run the application** 

    Run the following command to build and start all services.
    ```bash
    docker-compose up --build
    ```

5. ⚠️ **[Optional Troubleshooting]** 

    While running the `docker-compose up --build` if you get any error creating the fronend service regarding the `rollup-linux-arm64-musl`, try running the following command
    ```bash
    docker compose run frontend npm i && docker compose up
    ```
6.  🎉 **Access the servers**
  
     - **FE server**: localhost:5173
     - **BE API Docs**: localhost:8000/docs
7. 🔴 **Stopping the Application**
   
   ```
   docker-compose down
   ```

## Additional Information

### API Endpoints

  - **Key Endpoints**
    - Create task: POST /tasks/
    - Get all tasks: GET /tasks/
    - Get a single task: GET /tasks/{task_id}
    - Update task: PUT /tasks/{task_id}
    - Delete task: DELETE /tasks/{task_id}

### Some Useful Docker Commands for troubleshooting 🐋🐋🐋

```bash
docker remove [container-name]
docker ps
docker stop [container-name]
docker logs [container-name]
docker inspect [container-name]
```

### Improvement Ideas

- Filter based on complete/incomplete tasks
- Improve search incorporating backend and database
- Confirmation modal while deleting a task (Are you sure?)
- Showing Banner/alert after creating, updating, deleting a task (successful banner)
- Writing Tests
