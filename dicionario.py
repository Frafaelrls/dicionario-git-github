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
                  'git pull': '\ngit pull\nEnvio dos commits do repositório '
                              'remoto para o repositório local.',
                  'git reset': '\ngit reset [arquivo]\nRetira da seleção do '
                               'arquivo preservando o seu conteúdo.\n\n'
                               'git reset --hard [hash] \nRetorna para o '
                               'commit escolhido apagando todas as '
                               'modificações feitas após ele.\nNão é '
                               'recomendado usar no branch principal, com a '
                               'exclusão do histórico de commits poderá gerar '
                               'conflitos.\n\n'
                               'git reset --soft [hash] \nRetorna para o '
                               'commit escolhido mantendo salvos aparte as '
                               'modificações feitas após o commit escolhido. '
                               '\nNão é recomendado usar no branch principal, '
                               'com a exclusão do histórico de commits poderá '
                               'gerar conflitos.',
                  'git commit': '\ngit commit -m "mensagem" \nComando para '
                                'fazer o commit, usar uma mensagem breve no '
                                'imperativo.\n\ngit commit --amend '
                                '\nUsado para editar um commit, para commits '
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
                               ' commits.',
                  'snapshot': '\nsnapshot\nPrint do estado do arquivo naquele'
                              ' momento.',
                  'git revert': '\ngit revert [hash]\nComando para reverter '
                                'um commit sem alterar o histórico é '
                                'recomendado usar sempre que precisar reverter'
                                '.algo no branch master.',
                  'git log': '\ngit log\nVerifica os commits existentes e '
                             'pode-se pegar as rash.\n\ngit log -[numero]'
                             '\nApresenta uma quantidade específica de commits'
                             '.\n\ngit log --pretty=oneline\nApresenta o log '
                             'em uma linha única.\n\n'
                             'git log --pretty=oneline --graph\nApresenta em '
                             'gráfico os commits do branch atual.\n\n'
                             'git log --pretty=oneline --graph --all'
                             '\nApresenta em gráfico os commits de todos os'
                             " branch.\n\ngit log --since='[data]'\nApresenta "
                             'todos os commits a partir da data escolhida.\n\n'
                             "git log --until='[data]' \nApresenta os commits"
                             ' até essa data.\n\n'
                             "git log --since='[data1]' --until='[data2]'" 
                             '\nApresenta os commits no intervalo de datas '
                             'escolhidas, sendo excludente, busca entre as '
                             'datas mas não inclui commits nos dias escolhidos'
                             ".\n\ngit log --author='[nome]' \nFiltra os"
                             ' commits por nome do autor.',
                  'git show': '\ngit show [hash]\nExibe o que foi modificado '
                              'em um commit buscando pela hash.',
                  'git cherry-pick': '\ngit cherry-pick [hash]\nAtualiza um'
                                     ' commit especifico de uma branch em '
                                     'outra usando a hash como referência.',
                  'git rebase': '\ngit rebase -i head~2 \nModo interativo para'
                                ' trabalhar com os dois últimos commits.\n\n'
                                'git rebase -i --autosquash\nUne os commits '
                                'criados usando o "--fixup".\n\n'
                                'git rebase --continue\nContinua o rebase após'
                                ' a resolução de conflitos de commits.',
                  'git archive': '\ngit archive [nome do branch] --format=zip'
                                 ' --output[nome do arquivo]\nCria um ficheiro'
                                 ' compactado com todo o repositório.',
                  'git shortlog': '\ngit shortlog\nApresenta um log curto com'
                                  ' a quantidade total de commits por autor e'
                                  ' seus títulos.\n\ngit shortlog -sn\n'
                                  'Apresenta apenas a quantidade total de '
                                  'commits por autor.',
                  'git reflog': '\ngit reflog\nApresenta todas as referências'
                                ' de trabalhos feitos no git, apresentando os'
                                ' log mesmo após o uso de "git reset --hard",'
                                ' o que possibilita a recuperação de mudanças'
                                ' após o reset.',
                  'hash': '\nhash \nCódigo único de identificação dos commits'
                          ' é composto por números e letras.\n'
                          'Exemplo: 6d1fb45d01c596a7f6165ec834bb26b67650ffd6'}

    return dicionario
