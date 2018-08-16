FROM docker.dg-atlas.com:5000/ubuntu:1404
MAINTAINER xinjiayang@deepglint.com
RUN mkdir /demo
ADD demo /demo
RUN mkdir /demo/conf
ADD conf /demo/conf
WORKDIR /demo
