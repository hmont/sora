from __future__ import annotations

from typing import Any
from typing import Union

from sqlalchemy.sql.expression import ClauseElement

MySQLQuery = Union[str, ClauseElement]
MySQLParams = dict[str, Any] | None
MySQLRow = dict[str, Any]