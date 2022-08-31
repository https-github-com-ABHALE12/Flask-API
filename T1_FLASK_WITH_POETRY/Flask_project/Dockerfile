# start by pulling the python image
FROM alpine:latest

#to instal python3 and pip3 in docker image run apk add--no-cache python3 py3-pip
# RUN pip3 install --no-cache --upgrade pip setuptools
RUN apk add --no-cache --update python3-dev \ && pip3 install --upgrade pip 

# copy the requirements file into the image
# COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app            #create folder named app 
COPY . /app

# install the dependencies and packages in the requirements file
RUN pip3 --no-cache-dir install -r requirements.txt

# copy every content from the local file to the image
# COPY . /app
EXPOSE 5000

# configure the container to run in an executed manner
ENTRYPOINT [ "python3" ]   # when everything is created run python file 

# CMD : It is arguemts to ENTRYPOINT command 
CMD [ "app.py" ]
