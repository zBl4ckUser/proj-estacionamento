# Estaciona+

 Estaciona+ é um software de gestão de estacionamento criado como um projeto de estudo.


### Modo de uso
Caso esteja no Linux, execute o programa com o seguinte comando no terminal

```bash
$ python src/main.py
```
No Windows, clique duas vezes no arquivo main.py localizado na pasta `src`

------------

### Dependências

Este projeto tem como dependências os seguintes pacotes
> * PySide6
> * pyinstaller

Tais dependências podem ser instaladas com o seguinte comando:
```bash
$ python -m venv .venv/
$ source .venv/bin/activate 
$ pip install -r requirements.txt
```
### Versão de produção

Execute esse comando para criar o executável do projeto
```bash
$ pyinstaller --name="Estaciona+" -w src/main.py
```
O arquivo executável estará no diretório `dist`

Para o desenvolvimento desse software foi utilizado a linguagem Python na versão 3.10.12