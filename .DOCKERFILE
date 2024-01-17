FROM alpine
RUN apk add --update python3 py-pip
COPY . /exam
WORKDIR /exam
ENTRYPOINT ["python"]
CMD ["exam.py"]
