import re

WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")
TAG_PATTERN = re.compile(r"(?:^|\s)#([a-zA-Z\u4e00-\u9fff][\w\u4e00-\u9fff-]*)")
LINK_ALIAS_PATTERN = re.compile(r"\[\[([^|#\]]+)(?:\|([^\]]+))?\]\]")


def extract_wiki_links(content: str) -> list[dict[str, str]]:
    results = []
    for match in LINK_ALIAS_PATTERN.finditer(content):
        target = match.group(1).strip()
        alias = match.group(2).strip() if match.group(2) else target
        section = None
        if "#" in target:
            target, section = target.split("#", 1)
        results.append({
            "target": target,
            "alias": alias,
            "section": section,
        })
    return results


def extract_tags(content: str) -> list[str]:
    return [tag for tag in TAG_PATTERN.findall(content)]


def extract_excerpt(content: str, max_length: int = 200) -> str:
    text = re.sub(r"[#*`~\[\]()!>]", "", content)
    text = re.sub(r"\n+", " ", text).strip()
    if len(text) > max_length:
        text = text[:max_length].rstrip() + "..."
    return text


def count_words(content: str) -> int:
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", content))
    english_words = len(re.findall(r"[a-zA-Z]+", content))
    return chinese_chars + english_words
