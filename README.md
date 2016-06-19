# Projeto MAC0329

- Artur Alvarez		9292931
- Bruno Arico         8125459
- Gabriel Capella     8962078
- Nicolas Nogueira    9277541

### Estrutura do Projeto

A terceira parte do projeto consiste no acabamento do nosso computador HIPO.

Para realizar o acabamento foi necessário retrabalhar o FDX da parte 2 para acoplar uma ALU de 16 bits. Foi implementado uma forma de input/output com auxílio de uma pseudolinguagem interpretada por python que gera a entrada para o logisim.

### Acabamento do computador HIPO

Para o acabamento de nosso computador HIPO, três tarefas foram realizadas:

1. acoplamento da ALU de 16 bits na arquitetura de ciclo de instrução;
2. implementação de desvios condicionais;
3. funcionalidades de entrada/saída (I/O).

#### Acoplamento da ALU

A estrutura da ALU da primeira fase foi modificada de dois modos:

- As entradas passaram a ser de 16 bits e não mais 8 bits.
- O valor da saída da ALU somente é alterado se a mesma estiver habilitada pelo controlador. Isso permite, por exemplo, que após uma soma de dois números (operação que exige o acumulador em modo de leitura como uma das entradas da ALU), o valor resultante possa ser guardado no acumulador (operação que exige o acumulador em modo de escrita, ligado na saída da ALU).

Além da indicação de transbordamento (overflow), passamos também a indicar a ocorrência de divisão por zero. Na ocorrência de transbordamento e/ou divisão por zero, a execução do programa é interrompida. Para as modificações da ALU, foram utilizados os módulos aritméticos do Logisim.

O acoplamento da ALU com o ciclo de instrução nos permite a implementação das instruções correspondentes às cinco operações aritméticas:

       Código           | Instrução |                     Descrição
 Decimal |  Hexadecimal |           |
--------------------------------------------------------------------------------------------
   21    |     0x15     | {ADD} XY  | Soma ACC com conteúdo do endereço XY
   22    |     0x16     | {SUB} XY  | Subtrai conteúdo do endereço XY de ACC
   23    |     0x17     | {MUL} XY  | Multiplica ACC pelo conteúdo do endereço XY
   24    |     0x18     | {DIV} XY  | Divide ACC pelo conteúdo do endereço XY