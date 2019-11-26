# T2-SD-Temperaturas

##Para executar
- Abra um terminal e execute python3 server.py
	- Informe quantas salas serão geradas
- Abra outro terminal e execute python3 consumidor.py
	- Para cada sala, um terminal do tipo consumidor deve ser executado
	- O número da sala a ser feita a média deve ser informado
- Abra outro terminal e execute python3 cliente.py
	- Depois de 10 loops executando, o programa perguntará se o cliente deseja gerar o txt com o log de médias
		- Se o cliente digitar "s", o arquivo salvara o log de medias das salas em um txt chamado "medias" 
		- Se o cliente digitar "n", a etapa se repete após 10 loops