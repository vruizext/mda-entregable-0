# MDA - Entregable 0

## Maggie level

Dockerized python app that fetches quotes from The Simpsons Quote API and saves them to CSV format.
Also contains a Jupyter notebook used to set up and test the code to fetch the data from the API 
and save to file.

1. Go to `maggie` folder. 
```
$ cd maggie
```

2. Build docker image. 
```
$ docker build . -t maggie
```

4. Run image.
```
$ docker run -it -d maggie
```

5. Start bash terminal in the container.
```
$ docker exec -it {container_id} /bin/bash
```

6. Open quotes files
```
$ cat lisa/quotes.csv 

$ cat homer/quotes.csv

cat general/quotes.csv  
```


## Lisa level

Same as the previous, but it saves quotes from each character in a directory
with the character's name. Besides the quotes, inside each folder there is a JSON
file containing the word count for all the quotes collected for each character; and 
the character's image downloaded using the URL provided by the API.


1. Go to `lisa` folder. 
```
$ cd lisa
```

2. Build docker image. 
```
$ docker build . -t lisa
```

4. Run image.
```
$ docker run -it -d lisa
```

5. Start bash terminal in the container.
```
$ docker exec -it {container_id} /bin/bash
```

6. Inspect characters folders
```
$ ls -la app

$ ls -la 'Homer Simpson'
$ cat 'Homer Simpson'/quotes.csv
$ cat 'Homer Simpson'/counter.json
```


## Bart level

Multi-container app, composed of the Lisa app from previous step and a
jupyter notebook container to visualise folder contents and word counts. 

1. Go to `bart` folder. 
```
$ cd bart
```

2. Run containers. 
```
$ docker compose up
```

4. Go to notebook, using the URL that appears in the console.
```
http://127.0.0.1:8888/lab?token={your token}
```
