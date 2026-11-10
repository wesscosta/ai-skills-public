# AI Skills — Public

Coleção de **skills aprovadas para distribuição** a agentes de IA. Cada skill possui responsabilidade definida, gatilhos precisos e instruções reutilizáveis no formato [Agent Skills](https://agentskills.io/specification).

> **Situação atual:** nenhuma skill foi aprovada para publicação. As alterações de estrutura e validação não significam homologação de conteúdo.

## Estrutura

```text
skills/
  nome-da-skill/
    SKILL.md              # núcleo portável
    references/           # opcional: referência sob demanda
    templates/            # opcional: modelos
    examples/             # opcional: demonstrações
    scripts/              # opcional: automação testável
```

O nome da pasta deve corresponder ao `name` do frontmatter. Prefira uma skill pequena por responsabilidade, em vez de um prompt gigante. Divida componentes só quando cumprirem finalidades distintas.

## Como usar depois que uma skill for publicada

**Claude Code:** instale `skills/<slug>/` em `.claude/skills/<slug>/` do projeto ou no diretório pessoal suportado, e invoque a skill pelo nome quando disponível.

**ChatGPT:** importe a skill no recurso de Agent Skills disponível para o seu ambiente, ou compartilhe `SKILL.md` e referências em um Projeto/conversa como instruções manuais. Nem toda interface oferece instalação ou invocação automática.

**Outros agentes:** siga a instalação específica do produto. Compatibilidade estrutural não garante suporte a ferramentas, prompts especiais ou chamadas de comando.

## Qualidade e governança

- Desenvolvimento e testes ocorrem no repositório **privado** `wesscosta/ai-skills`.
- O catálogo Notion registra versões e estados; `Em validação` não significa aprovação.
- A distribuição exige aprovação expressa, revisão de licença, dependências, privacidade e segurança.
- O exportador privado usa allowlist. Somente arquivos revisados devem chegar ao repositório público.
- Não compartilhar logs privados, históricos de sessão, credenciais, dados de estudantes ou materiais restritos.

Validar a estrutura pública com:

```bash
python3 scripts/validate_public.py
```

Esse verificador não certifica segurança completa, eficácia pedagógica nem compatibilidade funcional entre ferramentas.

Consulte [CONTRIBUTING.md](CONTRIBUTING.md) e [SECURITY.md](SECURITY.md).
