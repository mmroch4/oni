# 💡 _Scripts_ ONI

Este repositório contém **propostas de resoluções** para os problemas **introdutórios** e **qualificatórios** das _[Olimpíadas Nacionais de Informática (ONI)](https://oni.dcc.fc.up.pt/)_.

Atualmente, este projeto contém apenas scripts em _**Python**_. Porém, num futuro próximo, serão também adicionados scripts em outras linguagens aceites pela organização do concurso (_**C**_, _**C++**_, _**Java**_, etc).

Espero que este compilado possa vos ajudar na vossa preparação :)

Sintam-se a vontade para contribuir 😁

## Como utilizar

Dentro do diretório de cada problema, existe um sub-diretório _**tests**_ e um ficheiro _**index.py**_. Este contém ficheiros `.txt` que correspondem a inputs relativos ao problema em questão, disponíveis no enunciado de cada problema.

Para testar a resolução de cada problema, execute o seguinte comando:

```bash
python3 index.py < ./tests/input-1.txt
```

- `index.py` corresponde ao ficheiro `.py` da resolução do exercício
- `./tests/input-1.text` corresponde ao ficheiro `.txt` que contém o input a testar
