FROM python:3.9.6

WORKDIR /code

RUN apt-get update
RUN apt-get install -y wget
RUN apt-key del 7fa2af80
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/cuda-keyring_1.0-1_all.deb
RUN dpkg -i cuda-keyring_1.0-1_all.deb
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub

RUN pip install -U notigram
ENV PYHTONUNBUFFERED=1
RUN export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/cuda/lib64

COPY ./ /code
RUN python -m pip install --upgrade pip
RUN pip install -U --no-cache-dir -r /code/requirements.txt
RUN python -m decompress Citas_RN.zip /code/Citas_RN.h5
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]