# definindo variáveis
NOME_IMAGEM="meuapp"
NOME_CONTAINER="media-calvex"
PORTA=5000

#construir a imagem docker
echo "construindo a imagem do docker..."
sudo docker build -t $NOME_IMAGEM .

#verificar se o container existe e esta em execução e se necessário pará-lo
if [ "$(sudo docker ps -q -f name=$NOME_CONTAINER)" ]; then
        echo "parando o container..."
        sudo docker stop $NOME_CONTAINER
fi


if [ "$(sudo docker ps -aq -f name=$NOME_CONTAINER)" ]; then
        echo "removendo o container..."
        sudo docker rm $NOME_CONTAINER
fi



#executando container
echo "iniciando o container"
sudo docker run -d --name $NOME_CONTAINER -p $PORTA:$PORTA $NOME_IMAGEM

