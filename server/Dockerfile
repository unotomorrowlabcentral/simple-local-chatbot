FROM python:3.12

# setworking dir
WORKDIR /server

# copy requirements
COPY requirements.txt  ./

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

# copy code 
COPY . .

# expose port within container
EXPOSE 8000

# entrypoint
CMD ["fastapi", "run", "server.py"]