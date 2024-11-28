Projeto Desligamento SESUITE 

Documentação do Processo  

Descrição: Pega dados das respostas das Entrevistas de Desligamento e joga para o SE.  

Última Atualização: Outubro 29, 2024 

Escrito por: Jhonny Anthony de Souza 

Informações de contato: ✉️ jhonny.souza@fgmdentalgroup.com  

 

Liberação: Projeto validado por Valter Mendes de Moura, Rejane Ribeiro Bonifacio,  Kemilyn Tuani da Silveira Maires 

Assinatura De Liberação: 

Valter Mendes de Moura: 

Rejane Ribeiro Bonifacio: 

Kemilyn Tuani da Silveira Maires: 

Visão Geral  

Informações do projeto  

 

Nome do projeto  

Projeto Desligamento SESUITE 

Proprietário do projeto  

FGM Dental Group 

Versão  

1.0  

Data  

DD/MM/YYYY  

 

Propósito  

O principal propósito do projeto foi garantir que dados de pessoas não sejam compartilhados, uso anterior era contra a LGPD (Lei Geral de Proteção de Dados) 

 

Atores envolvidos  

Jhonny Anthony de Souza, Desenvolvimento 

Adriano Elsenbach Guerra, Desenvolvimento e Ajudas 

Passos de Processo  

Lista os passos envolvidos no processo de forma clara e sequencial. 

 

1. Estrutura do Projeto  

 

Resumo  

 

Criar forms para testes 

Ler Forms 

Api  OneDrive 

Enviar dados para o SE 

Enviar dados com Registro de variáveis 

Validar a diferença de dados enviados para SE 

Verificar se tem nomes já cadastrados 

Caso tenha, validar por data de desligamento 

Fechar 

Envio de Logs 

 

 

 

 

Descrição da Estrutura 

 

Resumo 

Pensar na lógica e Desenvolvimento do código. 

Por quê? 

Garantir a qualidade e estruturação do desenvolvimento. 

Atores 

Jhonny Anthony de Souza,  

Adriano Elsenbach Guerra 

 

Resumo 

Criar Forms para testes 

Por quê? 

Criado para poder ter uma maneira de testar o código sem usar dados reais 

Ator 

Jhonny Anthony de Souza 

 

Resumo 

Ler o Forms 

Por quê? 

Feito para pegar dados das respostas 

Ator : Jhonny Anthony de Souza 

Resumo 

Enviar dados para o SE 

Por quê? 

Enviar dados ainda não prontos para testar conexão 

Ator 

Jhonny Anthony de Souza 

 

 

Resumo 

Validação dos dados do SE 

Por quê? 

Garantir que os dados não sejam duplicados. 

Atores 

Jhonny Anthony de Souza,  

Adriano Elsenbach Guerra 

 

Resumo 

Finalizar workflow quando tudo pronto. 

Por quê? 

Garantir o workflow seja fechado quando tudo validado. 

Ator 

Jhonny Anthony de Souza 

 

 

Regras  

Regras utilizadas para o desenvolvimento  

Regra 1  

Garantir que a segurança dos dados. 

Regra 2 

Garantir que a dados sejam feitos sem erros e sem duplicações. 

Regra 3  

Garantir que a estrutura do código seja limpa e reutilizável. 

 

Recursos Obrigatórios de Desenvolvimento 

 

Lista de todos os recursos ou ferramentas necessárias para executar o processo eficazmente. Isto pode incluir bibliotecas, e dados específicos. 

Recursos  

Informações  

Recurso 1  

Arquivo de requisitos para baixar bibliotecas necessárias. 

Recurso 2 

Env com dados sensíveis, compartilhada com o gestor de ti.  

Histórico de Revisões  

Data  

Descrição da revisão  

DD/MM/AAAA  

Descrição das alterações  

 

Onde Será armazenado 

 

O projeto será armazenado no servidor FGMVS0011SE, onde foi feito um agendador de tarefas que será usado para rodar o projeto de 15 em 15 dias. 

Como foi feito 

 

Algumas mudanças de path foram feitas para funcionar no servidor; 

Clonado repositório do GitHub que está armazenado o código; 

Adicionado ao disco local C -> C:\ProjectFormSE; 

Criada pasta “Script” no agendador de Tarefas no servidor; 

Feita ação de inicialização  
 
