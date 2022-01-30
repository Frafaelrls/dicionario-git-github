def dic():
    dicionario = {'git push': 'Envia as alterações locais para repositório.'
                              ' remoto.',
                  'git status': 'Lista todos os arquivos novos ou modificados'
                                ' para serem commitados.',
                  'git diff': 'Mostra diferenças no arquivo que não foram '
                              'realizadas.\n$ git diff --staged\n'
                              'Mostra a diferença entre arquivos selecionados'
                              ' e a suas últimas versões',
                  'git add': 'Faz o snapshot de um arquivo na preparação '
                             'para versionamento. $ git add [arquivo]',
                  'snapshot': 'Print do estado do arquivo naquele momento.',
                  'git pull': 'Envio dos commits do repositório remoto '
                              'para o repositório local.',
                  'git reset': 'Deseleciona o arquivo, mas preserva seu '
                               'conteúdo. $ git reset [arquivo]',
                  'git commit': 'Grava o snapshot permanentemente do arquivo '
                                'no histórico de versão. '
                                '$ git commit -m "[mensagem descritiva]"',
                  'git config': '$ git config --global user.name "[nome]"'
                                '\nConfigura o nome que você quer ligado as '
                                'suas transações de commit.'
                                '\n$ git config --global user.email '
                                '"[endereco-de-email]"'
                                '\nConfigura o email que você quer ligado as '
                                'suas transações de commit.',
                  'git branch': 'Lista todos os branches locais no repositório'
                                ' atual.\n$ git branch [nome-do-branch]\nCria '
                                'um novo branch\n$ git branch -d '
                                '[nome-do-branch]\nExclui o branch '
                                'específico.',
                  'git init': 'Cria um novo repositório local com um nome '
                              'específico. $ git init [nome-do-projeto]',
                  'git clone': 'Baixa um projeto e seu histórico de versão '
                               'inteiro. $ git clone [url]',
                  'git checkout': 'Muda para o branch específico e atualiza o '
                                  'diretório de trabalho. $ git checkout '
                                  '[nome-do-branch]',
                  'git merge': 'Combina o histórico do branch específico com o'
                               ' branch atual. $ git merge [branch]'}

    return dicionario
