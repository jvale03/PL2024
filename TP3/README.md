# TPC3: Somador on/off
## Aluno: 
- João Carlos Oliveira Vale 
- a100697

## Resumo

Para o desenvolvimento deste somador, usaremos as expressões regulares através da biblioteca ***re*** do python.

1. Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
2. Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
3. Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
4. Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.

Para a realização deste exercício, comecei por usar o módulo `re.findall()` para encontrar todas as ocorrências desejadas. Após isso é tão 
simples quanto percorrer todas as ocorrências com um *for loop* e, usando `re.match()`, realizar as operações exigidas no enunciado.  