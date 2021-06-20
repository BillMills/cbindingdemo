FROM ubuntu:20.04
RUN apt-get update -y && DEBIAN_FRONTEND=noninteractive apt-get install -y nano git wget build-essential g++ python3-dev autotools-dev libicu-dev build-essential libbz2-dev libboost-all-dev
RUN mv /usr/bin/python3 /usr/bin/python

WORKDIR /boost
RUN wget https://boostorg.jfrog.io/artifactory/main/release/1.76.0/source/boost_1_76_0.tar.gz
RUN tar -xzvf boost_1_76_0.tar.gz
RUN cd /boost/boost_1_76_0 && ./bootstrap.sh --with-libraries=python && ./b2 install

# then to build some c++ into a python extension,
# make some xxx.cpp per the examples, and:
# g++  -fPIC -shared -I /usr/include/python3.8/ hello.cpp -o hello.so -lboost_python38
# then `include hello` will work in python and expose your functions.
# more detailed numpy-leveraging example at https://cosmiccoding.com.au/tutorials/boost
