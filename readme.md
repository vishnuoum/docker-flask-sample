# ML Model Docker Deployment Project

A Python based project written in flask to study the docker image building and sample deployment

## Explanation on Dockerfile

```
FROM python:3.10                                         # Base image used for build
WORKDIR /code                                            # Specify the work directory within the container
COPY requirements.txt .                                  # Copy requirement file to container
RUN pip3 install -r requirements.txt --progress-bar=off  # Run pip install
COPY /code .                                             # Copy the code base to the container work directory
EXPOSE 5000                                              # Expose the port of container for requests
ENTRYPOINT ["python","app.py"]                           # Start the application
```

## Building the docker image

```
docker build -t <image-name> .
```

## Running the container from local docker image

```
docker run --name <name of container> -dp 5000:5000 <image-name>
```