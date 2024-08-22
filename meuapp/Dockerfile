#imagem do python que vamos utilzae
FROM python:3.12

#diretorio de trabalho do container
WORKDIR /app

#instalar as dependencias
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

#Copiando os arquivos para o docker
COPY . .

#Rodando nossa aplicação
CMD ["python", "app.py"]

