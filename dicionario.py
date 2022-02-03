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
                  'git add': '\ngit add .\nAdiciona todos os arquivos '
                             'modificados para serem commitados.\n\n'
                             'git add [nome do arquivo] \nAdiciona o arquivo '
                             'listado para ser commitado.\n\n'
                             'git add -p \npermite dividir em partes '
                             'modificações realizadas em um arquivo, criando '
                             'dois ou mais commits.',
                  'snapshot': '\nsnapshot\nPrint do estado do arquivo naquele'
                              ' momento.',
                  'git pull': '\ngit pull\nEnvio dos commits do repositório '
                              'remoto para o repositório local.',
                  'git reset': '\ngit reset [arquivo]\nDesselecionar o arquivo'
                               'mas preserva seu conteúdo.',
                  'git commit': '\ngit commit -m "mensagem" \nComando para '
                                'fazer o commit, usar uma mensagem breve no '
                                'imperativo.\n\ngit commit --amend '
                                '\nUsado para editar um commit, para commites '
                                'do master usar antes de enviar para o '
                                'repositório remoto para evitar o surgimento '
                                'de conflito de histórico.\n\n'
                                'git commit --fixup [hash] \n'
                                'Aplica correção de um commit.',
                  'git config': '\ngit config --global user.name "[nome]"'
                                '\nConfigura o nome que você quer ligado as '
                                'suas transações de commit.\n\n'
                                'git config --global user.email '
                                '"[endereço-de-email]"\n'
                                'Configura o email que você quer ligado as '
                                'suas transações de commit.\n\n'
                                'git config --global help.autocorrect 1\n'
                                'Ativa a função de corretor de digitação de '
                                'comandos do git Ex: "git stratus" será '
                                'interpretado como "git status".',
                  'git branch': '\ngit branch \nLista todos os branches locais'
                                ' no repositório atual.\n\n'
                                'git branch [nome do branch]\n'
                                'Cria um novo branch\n\ngit branch -b '
                                '[nome do branch]\nExclui o branch '
                                'específico, não pode deletar um branch ativo.'
                                '\n\ngit branch -d [nome do branch]\n'
                                'Força a exclusão do branch.',
                  'git init': '\ngit init [nome do projeto]\nCria um novo'
                              ' repositório local com um nome específico.',
                  'git clone': '\ngit clone [url]\nBaixa um projeto e seu '
                               'histórico de versão.',
                  'git checkout': '\ngit checkout -b [nome do branch] '
                                  '\nCria um novo branch.\n\n'
                                  'git checkout [nome do branch]\nMuda para o '
                                  'branch específico e atualiza o diretório de'
                                  ' trabalho.\n\ngit checkout -\nRetorna para '
                                  'o ultimo branch acessado.',
                  'git merge': '\ngit marge [nome do branch]\nCombina o '
                               'histórico do branch específico com o branch'
                               ' atual.\n\ngit marge --continue\nContinua o '
                               'merge após a resolução de conflitos de'
                               ' commits.'}

    return dicionario
