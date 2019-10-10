
i=0

docker ps -a |while read line
do
	if((i>0)) 
	then
		containerid=`echo $line|cut -d " " -f1`
		image=`echo $line|cut -d " " -f2`
		docker rm $containerid
		docker rmi $image
		echo $containerid
		echo $image
	fi
	((i++))
done

docker-compose up
