# dockerfile, image ,container
FROM python:3.11.2-alpine3.17

RUN mkdir /project
WORKDIR /project

COPY . .
RUN pip3 install -r requirement.txt
RUN python db.py

ENTRYPOINT [ "python", "-m", "flask", "run", "--host=0.0.0.0" ]
