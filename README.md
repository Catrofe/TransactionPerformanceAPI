# TransactionPerformanceAPI

Performance em python?<br>
Exatamente isso e nesse README irei descrever como fiz, decisões que tomei e porque tomei essas decisões e o quanto estou satisfeito com meu resultado, LETS GO?

## Explicando cenários de teste simples

Proposta: Você irá inserir em um endpoint post um json com dois itens, exemplo

```json
{
  "stock_code": ["ITAUSA4", "IBOV", "SOMA3", "ITAU3", "ITAU4", "PETR4"],
  "amount_of_stocks": 15000
}
```

**O que você está dizendo para a API?** <br>
Simples, você está dizendo para ela gerar *15.000* falsas transações aleatoriamente com a lista de stock_code que você informou. <br>

Eu sei que 15.000 não é um número elevado, porem esse foi meu cenário inicial.

## Primeiro cenário de 15k Transações
Commit: https://github.com/Catrofe/TransactionPerformanceAPI/tree/aca7d721c70f743099b12de51345129b2093e4a3

Esse primeiro cenário foi o mais caótico, mesmo usando o fastapi asyncronamente eu recebi resultados de no minímo 30 segundos, era um desastre completo visto que muitos sistemas devolvem TimeOut com apenas 15 segundos, alguns com 30 segundos e outros com 60 segundos.

Meu código era longe de ser performático e eu precisava resolver isso.


## Segundo cenário de 15k Transações
Commit: https://github.com/Catrofe/TransactionPerformanceAPI/tree/c32a31b0dc4bd611d2650c54ac0266ab1110017a

Esse foi meu segundo cenário onde obtive médias de 11 segundos, nossa fiquei super feliz em conseguir reduzir 20 segundos por chamada quase, apenas otimizando meu service.<BR>
Como cheguei nesse resultado? Sei que consigo extrair mais do meu sistema e melhorar minha performance e fui testando diversas soluções a que melhor se adaptou aos meus requisitos foi o **asyncio.gather** que fez com a performance subisse bizarramente.
O Asyncio.gather faz com que objetos aguardaveis sejam executados de forma concorrente e dessa forma reduziu o tempo de execução.


## Terceiro cenário de 15k Transações
Commit: https://github.com/Catrofe/TransactionPerformanceAPI/tree/574a7d35798d09b62b7fdee868817d89707afbf8

Esse foi uma solução extremamente simples que não me orgulho em ter demorado a pensar. Até o momento meu código fazia o seguinte: <br>
- Eu gerava 1 transação e postava ela no banco e repetia esse processo 15.000 vezes. <br>

Não preciso falar o quanto isso é ineficiente, preciso?

A solução foi simples, eu gerei as 15.000 transações e persisti todas ao mesmo tempo no banco e pasmem, meu tempo caiu para **1,2** segundos.

Reduzi meu tempo em quase 90% e ainda assim acho que posso melhorar essa performance.


## Quarto cenário de 15k Transações
Commit: https://github.com/Catrofe/TransactionPerformanceAPI/tree/c894dc21b9a641ac7bf0274845a0a690a89c9c97

Bom, nessa solução voltamos ao banco de dados novamente. Ok, eu estava inserindo transação por transação e com certeza ele me odiou por isso, então eu forcei 15k de escritas de uma só vez. Nesse momento ele deve ter ficado um pouco mais contente porem ainda assim não era o ideal e novamente ele era meu gargalo.<br>
Consegui atingir cerca de **900ms** em alguns testes e eu estava bem feliz, porem não me sentia contente, o teste parecia não exibir o verdadeiro "potencial".<br>

Com base nisso aumentei para 100k requisições e no meu primeiro cenário eu tive cerca de 8 segundos de tempo de resposta. Isso foi tenebroso eu diria.
Voltei ao gargalo do banco e comecei a procurar formas de melhorar isso de diversas formas, por fim eu particionei a minha lista em 10k requisições que lidou muito bem com 15k, 100k requisições.


## Considerações finais até o momento

- 08/01/2024
  Nessa data eu ainda estou no Terceiro cenário, pretendo continuar estudando formas de melhorar cada vez mais a performance desse código dentro do aceitável. <br>
  Se eu conseguir farei um push e adicionarei a descrição do novo cenário.

-08/01/2024
  Tempos de resposta:
  - 15k -- 550ms
  - 100k 3.5s
