# World Of Games


# How to:

**Build:**

>  - docker-compose build

**Run:**

>  - docker-compose up -d

**Play the game:**

>  - docker exec -it wog python MainGame.py

**Run test:**

 > - docker exec -it wog python tests/e2e.py 
 > - Should return 0 if test pass -1 if not

**Clean:**

>  - docker-compose down;docker rmi $(docker images -q)

**Run Jenkins test:**

 - set the following environment variables :
	 - [ ] DOCKER_ID
	 - [ ] DOCKER_PASSWORD
 - Build pipeline script from scm


