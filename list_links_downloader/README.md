# Download de arquivos por lista
Neste algoritmo, o usuário deve fornecer um csv formatado da seguinte forma:
```bash
descricao_do_conteudo, link_do_conteudo
```
Exemplo:
```bash
descricao_do_conteudo, link_do_conteudo
Videozinho 1, http://www.videosengracados.com.br/Videozinho1.mp4
CD de musica, http://www.musicengracados.com.br/CD1.zip
```

Estando neste formato, o algoritmo vai receber e entender o que é para fazer, salvando a lista de arquivos da seguinte forma:

```
downloads
|__Videozinho1.mp4
|__CD1.zip
```
Se colocar o inverso, ele vai dar erro na linha e vai para a seguinte. Se caso o link para o download, por algum motivo, não existir, ele vai dar erro e vai mostrar o erro no próprio terminal.

## Como usar?

Para usar é simples: basta executar o comando `python main.py <nome_do_arquivo.csv>`. Uma vez que fizer isto, ele vai executar e iniciar o download, mostrando a progressão por arquivo.