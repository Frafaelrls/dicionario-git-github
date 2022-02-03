def dic():
    dicionario = {'git push': '\ngit push origin [nome do branch] \n'
                              'Envia o commit para o repositório online.\n\n'
                              'git push origin [nome do branch] -- force \n'
                              'Usar após ter sido usado o git reset, para '
                              'forçar o commit.\n\n'
                              'git push origin [nome do branch] -- rebase \n'
                              'Envia o commit e coloca ele no topo, evitando'
                              ' conflitos com outros commits.\n\n'
                              'git push origin [nome do branch] '
                              '--delete [nome do branch]  \n'
                              'Deleta no repositório remoto o branch '
                              'especificado.\n\n'
                              'git push origin master :[nome do branch] \n'
                              'Deleta no repositório remoto o branch'
                              ' especificado.',
                  'git status': '\nLista todos os arquivos novos ou '
                                'modificados para serem commitados.',
                  'git diff': '\ngit diff\nMostra diferenças no arquivo que '
                              'não foram realizadas.\n\ngit diff --staged\n'
                              'Mostra a diferença entre arquivos selecionados'
                              ' e a suas últimas versões.',
                  'git add': 'Faz o snapshot de um arquivo na preparação '
                             'para versionamento. $ git add [arquivo]',
                  'snapshot': 'Print do estado do arquivo naquele momento.',
                  'git pull': 'Envio dos commits do repositório remoto '
                              'para o repositório local.',
                  'git reset': 'Desselecionar o arquivo, mas preserva seu '
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
