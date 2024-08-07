# -*- coding: utf-8 -*-
import os

def find_files_with_keyword(directory, keyword):
    """
    Percorre os arquivos .py de um diretório e retorna uma lista dos arquivos que contêm a palavra-chave especificada.

    Args:
        directory (str): Caminho do diretório a ser percorrido.
        keyword (str): Palavra-chave a ser procurada nos arquivos.

    Returns:
        list: Lista de caminhos dos arquivos que contêm a palavra-chave.
    """
    matching_files = []
    
    # Percorre todos os arquivos do diretório e subdiretórios
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # Abre e lê o conteúdo do arquivo
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Verifica se a palavra-chave está no conteúdo do arquivo
                        if keyword in content:
                            matching_files.append(file_path)
                except Exception as e:
                    print(f"Erro ao ler o arquivo {file_path}: {e}")
    
    return matching_files

# Diretório a partir do qual começar a busca (raiz do projeto)
project_root_directory = os.path.dirname(os.path.abspath(__file__))
keyword_to_find = 'axial_position'

# Chama a função e exibe os arquivos encontrados
files_found = find_files_with_keyword(project_root_directory, keyword_to_find)
print(f'Arquivos que contêm a palavra "{keyword_to_find}":')
for file in files_found:
    print(file)
