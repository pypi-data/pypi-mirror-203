from typing import Optional, Dict, List

from .finder import _find_all, _find


class HTMLElement():
    def __init__(self,
                 tagname: str,
                 closed: bool = False,
                 attrs=None,
                 text: str = "",
                 descendants=[],
                 parent=None,
                 previous_sibling=None,
                 next_sibling=None,
                 _all_text=[],
                 _children=[]
                 ):
        self.tagname = tagname
        self.closed = closed
        self.attrs = attrs
        self.text = text
        self.descendants = descendants
        self.parent = parent
        self.previous_sibling = previous_sibling
        self.next_sibling = next_sibling
        self._all_text = _all_text
        self._children = _children

    def __repr__(self) -> str:
        return f"{self.tagname.upper()} attrs={self.attrs} text={self.text}"

    def find_all(self, tag: str, attrs: Optional[Dict[str, str | None]] = None, exclude_attrs: Optional[Dict[str, List[str | None]]] = None):
        """Return all matching elements"""
        return _find_all(self.descendants, tag, attrs, exclude_attrs)

    def find(self, tag: str, attrs: Optional[Dict[str, str | None]] = None, exclude_attrs: Optional[Dict[str, List[str | None]]] = None):
        """Return first matching element"""
        return _find(self.descendants, tag, attrs, exclude_attrs)

    @property
    def children(self) -> List:
        """Return elements one level down"""
        return reversed(self._children)

    @property
    def all_text(self) -> str:
        """Return all text within element"""
        res = ""
        for text_or_obj in self._all_text:
            if type(text_or_obj) == str:
                res += text_or_obj
                continue
            res += text_or_obj.all_text
        return res

    @property
    def previous_siblings(self):
        """Generate previous elements on the same level"""
        prev = self.previous_sibling
        while prev:
            yield prev
            prev = prev.previous_sibling

    @property
    def next_siblings(self):
        """Generate next elements on the same level"""
        nxt = self.next_sibling
        while nxt:
            yield nxt
            nxt = nxt.next_sibling

    @property
    def ancestors(self):
        """Generate all elements within element"""
        parent = self.parent
        while parent:
            yield parent
            parent = parent.parent
