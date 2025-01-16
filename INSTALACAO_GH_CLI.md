# Como Instalar o GitHub CLI (`gh`)

O GitHub CLI (`gh`) é uma ferramenta de linha de comando que permite interagir com o GitHub diretamente do terminal. Abaixo estão os passos para instalar o `gh` no **Windows**, **Linux** e **macOS**.

---

## 1. **Instalar no Windows**

### Usando o Instalador:
1. Acesse a página de releases do GitHub CLI: [https://github.com/cli/cli/releases](https://github.com/cli/cli/releases).
2. Baixe o instalador para Windows (arquivo `.msi`).
3. Execute o instalador e siga as instruções.

### Usando o Winget (Windows Package Manager):
Se você tem o **Winget** instalado (disponível no Windows 10+), pode instalar o `gh` diretamente pelo terminal:
```bash
winget install --id GitHub.cli
```

### Verificar a Instalação:
Abra o Prompt de Comando ou PowerShell e digite:

```bash
gh --version
```
Se a instalação foi bem-sucedida, você verá a versão do gh instalada.


## 2. Instalar no Linux
No Ubuntu/Debian:

Adicione a chave GPG do repositório:

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
```

Adicione o repositório à lista de fontes:

```bash

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
```
Atualize a lista de pacotes:
```bash
sudo apt update
```

Instale o gh:
```bash
sudo apt install gh
```
No Fedora:

Adicione o repositório:
```bash
sudo dnf config-manager --add-repo https://cli.github.com/packages/rpm/gh-cli.repo
```
Instale o gh:
```bash
sudo dnf install gh
```
No Arch Linux:

Instale o gh usando o pacote oficial:
```bash
sudo pacman -S github-cli
```
Verificar a Instalação:

No terminal, digite:
```bash
gh --version
```
Se a instalação foi bem-sucedida, você verá a versão do gh instalada.

## 3. Instalar no macOS
Usando o Homebrew (recomendado):
Se você ainda não tem o Homebrew instalado, instale-o:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Instale o gh:
```bash
brew install gh
```
Usando o Instalador Oficial:

- Acesse a página de releases do GitHub CLI: https://github.com/cli/cli/releases.
- Baixe o instalador para macOS (arquivo .pkg).
- Execute o instalador e siga as instruções.
- Verificar a Instalação:

No terminal, digite:
```bash
gh --version
```

Se a instalação foi bem-sucedida, você verá a versão do gh instalada.

# Autenticação no GitHub
Após instalar o gh, você precisa autenticar-se no GitHub para usar o CLI:

Execute o comando:
```bash
gh auth login
```
Siga as instruções:

- Escolha GitHub.com.
- Escolha Login via navegador (recomendado) ou Login com token.

Se optar pelo navegador, uma janela será aberta para você autorizar o acesso.

Se optar pelo token, você precisará gerar um token de acesso pessoal no GitHub e inseri-lo no terminal.

# Comandos Básicos do gh
Aqui estão alguns comandos úteis do gh:

Clonar um repositório:

```bash
gh repo clone <nome-do-repositorio>
```
Exemplo:
```bash
gh repo clone octocat/Hello-World
```

Criar um novo repositório:
```bash
gh repo create
```
Listar repositórios:
```bash
gh repo list
```
Abrir o repositório no navegador:
```bash
gh repo view --web
```

# Próximos Passos
Agora que você tem o GitHub CLI instalado, explore mais comandos e integrações para melhorar seu fluxo de trabalho com o GitHub. Para mais informações, consulte a documentação oficial do GitHub CLI.

