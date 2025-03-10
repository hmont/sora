from __future__ import annotations

from typing import Any
from typing import cast

from sqlalchemy.sql.compiler import Compiled

from sqlalchemy.sql.expression import ClauseElement

from sqlalchemy.dialects.mysql.mysqldb import MySQLDialect_mysqldb

from databases import Database as _Database

from app.core.types import MySQLParams
from app.core.types import MySQLRow
from app.core.types import MySQLQuery

DIALECT = MySQLDialect_mysqldb()

class Database:
    def __init__(self, dsn: str) -> None:
        self._db = _Database(dsn)


    def _compile(self, query: ClauseElement) -> tuple[str, MySQLParams]:
        compiled: Compiled = query.compile(
            dialect=DIALECT,
            compile_kwargs={
                "literal_binds": True,
                "render_postcompile": True
            }
        )

        return compiled.string, cast(MySQLParams, compiled.params)


    async def connect(self) -> None:
        await self._db.connect()


    async def disconnect(self) -> None:
        await self._db.disconnect()


    async def fetch_all(
        self,
        query: MySQLQuery,
        values: MySQLParams = None
    ) -> list[MySQLRow]:
        if isinstance(query, ClauseElement):
            query, values = self._compile(query)

        rows = await self._db.fetch_all(query, values)

        return [dict(row._mapping) for row in rows]


    async def fetch_one(
        self,
        query: MySQLQuery,
        values: MySQLParams = None
    ) -> MySQLRow | None:
        if isinstance(query, ClauseElement):
            query, values = self._compile(query)

        row = await self._db.fetch_one(query, values)

        return dict(row._mapping) if row else None


    async def execute(
        self,
        query: MySQLQuery,
        values: MySQLParams = None
    ) -> int:
        if isinstance(query, ClauseElement):
            query, values = self._compile(query)

        rec_id = await self._db.execute(query, values)

        return cast(int, rec_id)