# Contribuição e aprovação

Este repositório distribui **somente skills aprovadas**. A fonte de desenvolvimento é privada; propostas de melhoria podem ser discutidas em issues e PRs sem incluir dados sensíveis.

Para liberar uma skill:

1. Demonstrar escopo e gatilhos sem sobreposição com outras skills.
2. Validar frontmatter Agent Skills (`name`, `description`) e referências locais.
3. Ensaiar casos reais, negativos e limites das ferramentas em ao menos um ambiente aplicável.
4. Revisar segurança, dados pessoais, licenças, atribuição e dependências de terceiros.
5. Registrar aprovação de publicação no manifesto privado e inspecionar o diff de exportação.
6. Validar com `python3 scripts/validate_public.py` e CI antes do merge autorizado.

Nenhuma alteração em `main` nem publicação de conteúdo em produção sem aprovação. Um teste sintático bem-sucedido não comprova homologação.
