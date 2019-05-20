## Dockers

Once that you copy your aapp.py the Docker expects to see a DockerFile

- To create a DockerFile. In terminal write : touch Dockerfile

After that we nee to tell to Docker which applications that is necessary to run the Application app.py. For that we need create a file that contains the default libraries necessary by app.py.

- touch requirements.txt


## DockerFile
The DockerFile have the instructions to build a machine from scratch.

Open the DockerFile and fill with the next lines (without the comments after ->)

- FROM python:3 -> This pull pyhton 3 from https://hub.docker.com/_/pyhton/ that is like a a repository for dockers
                   The truth is that pulls the Ubuntu too to run the python3 in the container.

- WORKDIR /usr/src/app -> Defining the work directory (this path is just a convention)

- COPY requirements.txt . -> To copy to the current work directory the file that contains the specifications to install in the machine. Attention to the dot(.) at the end of the command line.

- RUN pip install --no-cache-dir -r requirements.txt -> Once tyou have the requirements.txt on the container you need install the specification that are inside of this file.

- COPY . . -> Copy all files of the current directory (local) first dot(.) to the machine, the second dot(.) means into the machine (container)

- CMD ["python", "app.py"] -> to run in the machine the app.py using python
                   
## requirements.txt
This file ontains the programs or libraries taht you need to run your application. For our case fill the file as

- flask
- flask_restful

That tells to pip to install this two libraries.

## Docker- Compose
Now we need to do something to automatically start this application. First we to jump to the main directory (Tutorial1) and create the docker-compose that contains all containers (imagine you have many containers: web,db,npl, etc.). The docker-compose controls this containers

- to create the yml file -> touch docker-compose.yml
