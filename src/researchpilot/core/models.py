from dataclasses import dataclass, field
@dataclass
class Finding:
    title: str; authors: list = field(default_factory=list); year: int = 0; summary: str = ""; keywords: list = field(default_factory=list); doi: str = ""
    def to_dict(self): return {"title": self.title, "authors": self.authors, "year": self.year, "summary": self.summary, "keywords": self.keywords, "doi": self.doi}
