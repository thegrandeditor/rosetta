from pydantic import BaseModel
from typing import List, Dict, Optional, Any


class TranspileRequest(BaseModel):
    source: str
    from_lang: str  # Extension e.g., '.py', '.sol', '.cbl', '.carbon'
    to_lang: str    # Identifier e.g., 'py', 'js', 'cpp', 'rs', 'go'


class TranspileResponse(BaseModel):
    result: str
    tokens_used: int
    time_ms: float
    ast: Optional[Any] = None
    passes: Optional[List[str]] = None


class DetectRequest(BaseModel):
    source: str


class DetectResponse(BaseModel):
    language: str
    confidence: float


class LanguageInfo(BaseModel):
    name: str
    ext: str
    phase: int
    paradigm: str
    glowColor: str
    sampleCode: str


class LanguagesResponse(BaseModel):
    languages: List[LanguageInfo]


class LearnRequest(BaseModel):
    grammar: Optional[str] = None
    bnf: Optional[str] = None
    corpus: Optional[str] = None
    name: Optional[str] = None


class LearnResponse(BaseModel):
    success: bool
    message: str
    language_id: Optional[str] = None
    ext: Optional[str] = None
