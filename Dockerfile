FROM python:3.7-stretch

WORKDIR /profile

ADD . /profile

# Install the dependencies
RUN pip install -r requirements.txt

COPY /profile .

RUN make /profile

CMD ["python", "profile/app.py"]

# docker build -t profile .
# docker run -p 5000:5000 profile
# docker images
# docker push jroc561/profile
