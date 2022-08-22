# used to fetch the base docker image
FROM laudio/pyodbc:1.0.4

# to install python3 and pip3 in docker image
#RUN apk add --no-cache python3 py3-pip

RUN pip3 install --no-cache --upgrade pip setuptools

#creating app folder inside image as present working directiory
WORKDIR /app

#It will copy all things from location where dockerfile is present into present working directory or app folder 
COPY . /app

# The requirement.txt file will copy into these particular app folder 
RUN python3 -m pip install -r /app/requirements

#we have to make container executable if we creating container from docker file then it should not be exit itself and it should be executable 
EXPOSE 5001

#ENTRYPOINT commands make the container executable .whatever command we have to run when we are creating docker container from your docker image
ENTRYPOINT ["python3"]

#CMD :It is arguments to ENTRYPOINT command

CMD ["app.py"]
