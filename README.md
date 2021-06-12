# RTMP Video Stream
This repository will be useful for anyone who wants to create a REST API for streaming an RTMP stream through a URL.

## Instructions
In order to run the project, follow the following steps:
1. Install Anaconda
2. Create a conda environment using the following code:
```
    conda create --name rtmp_stream anaconda python=3.8
```
3. Activate conda environment:
```
    conda activate rtmp_stream
```
4. Navigate to the parent folder
5. Install the required libraries:
```
    pip install -r requirements.txt
    conda install -c conda-forge uwsgi
```
6. Change the rtmp stream link in the app.py file
7. Run the following command to start the production server:
```
    uwsgi --module app:app --http :5000 --http-processes 4 --processes 1 --threads 50 --post-buffering 65535 --buffer-size 65535 --offload-threads 1
```
## Framework Used
Flask (Python)

### N.B.
Please ensure that the rtmp stream is working properly at first, before starting the streaming server. Otherwise, the server won't work properly