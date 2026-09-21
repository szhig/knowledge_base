from dataclasses import dataclass


@dataclass
class TextChunk:
    content: str
    chunk_index: int
    token_count: int
    metadata: dict


class RecursiveTextSplitter:
    """Recursively split text by paragraph → sentence → character."""

    def __init__(
        self,
        chunk_size: int = 512,
        chunk_overlap: int = 64,
        separators: list[str] | None = None,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", "。", ".", " ", ""]

    def split(self, text: str) -> list[TextChunk]:
        chunks: list[str] = []
        self._recursive_split(text, self.separators, chunks)

        # Merge small chunks and apply overlap
        merged = self._merge_chunks(chunks)

        return [
            TextChunk(
                content=c,
                chunk_index=i,
                token_count=len(c) // 4,
                metadata={},
            )
            for i, c in enumerate(merged)
        ]

    def _recursive_split(
        self, text: str, separators: list[str], result: list[str]
    ) -> None:
        if len(text) <= self.chunk_size:
            if text.strip():
                result.append(text.strip())
            return

        sep = separators[0] if separators else ""
        if sep == "":
            for i in range(0, len(text), self.chunk_size):
                chunk = text[i : i + self.chunk_size]
                if chunk.strip():
                    result.append(chunk.strip())
            return

        parts = text.split(sep)
        for part in parts:
            if len(part) > self.chunk_size and len(separators) > 1:
                self._recursive_split(part, separators[1:], result)
            elif part.strip():
                result.append(part.strip())

    def _merge_chunks(self, chunks: list[str]) -> list[str]:
        if not chunks:
            return []

        merged: list[str] = []
        current = chunks[0]

        for chunk in chunks[1:]:
            if len(current) + len(chunk) <= self.chunk_size:
                current = current + "\n\n" + chunk
            else:
                merged.append(current)
                if self.chunk_overlap > 0 and len(current) > self.chunk_overlap:
                    overlap = current[-self.chunk_overlap :]
                    current = overlap + "\n\n" + chunk
                else:
                    current = chunk

        merged.append(current)
        return merged
