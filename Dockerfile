FROM python:3
ADD authentication.py /
CMD [ "python", “./authentication.py" ]