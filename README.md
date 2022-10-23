# MDA - Entregable 0

## Maggie level

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
$ docker run -it -d maggie -e SLEEP_TIME=30
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
