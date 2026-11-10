#!/usr/bin/env python3
"""Verifica estrutura mínima de distribuição, sem publicar conteúdo."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "skills"
ALLOWED_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")


def validate() -> list[str]:
    errors = []
    if not DIRECTORY.exists():
        return errors
    for item in sorted(DIRECTORY.iterdir()):
        if item.name.startswith("."):
            continue
        if not item.is_dir() or item.is_symlink() or not ALLOWED_NAME.fullmatch(item.name):
            errors.append(f"Item inválido: {item}")
            continue
        skill_file = item / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"Sem SKILL.md: {item}")
            continue
        content = skill_file.read_text(encoding="utf-8")
        if not content.startswith("---\n") or content.count("---\n") < 2:
            errors.append(f"Frontmatter ausente/incompleto: {item}")
            continue
        header = content.split("---", 2)[1]
        name = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", header)
        desc = re.search(r"(?m)^description:\s*.+$", header)
        if not name or name.group(1) != item.name or not desc:
            errors.append(f"Nome ou descrição inválidos: {item}")
        for file in item.rglob("*"):
            if file.is_symlink():
                errors.append(f"Symlink não permitido: {file}")
            if file.is_file() and file.stat().st_size > 1_000_000:
                errors.append(f"Arquivo excessivo: {file}")
            if file.is_file() and file.suffix.lower() in (".md", ".txt", ".py", ".json"):
                try:
                    if PRIVATE_KEY.search(file.read_text(encoding="utf-8")):
                        errors.append(f"Chave privada encontrada: {file}")
                except UnicodeDecodeError:
                    errors.append(f"Arquivo textual inválido: {file}")
    return errors


if __name__ == "__main__":
    problems = validate()
    found = len(list(DIRECTORY.glob("*/SKILL.md"))) if DIRECTORY.exists() else 0
    print(f"Skills públicas encontradas: {found}")
    for issue in problems:
        print("ERRO:", issue)
    if not problems:
        print("Estrutura válida. Não implica homologação ou aprovação de publicação.")
    sys.exit(1 if problems else 0)
