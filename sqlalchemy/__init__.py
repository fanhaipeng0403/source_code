# sqlalchemy/__init__.py
# Copyright (C) 2005-2018 the SQLAlchemy authors and contributors
# <see AUTHORS file>
#
# This module is part of SQLAlchemy and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php


##### 数据库引擎，处理连接等
from .engine import create_engine, engine_from_config
###  检查监测功能，它在Core和ORM中提供有关各种SQLAlchemy对象的运行时信息。
from .inspection import inspect
#### 表的结构 ˈskiːmə
from .schema import (
    CheckConstraint,
    Column,
    ColumnDefault,
    Constraint,
    DefaultClause,
    FetchedValue,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    MetaData,
    PassiveDefault,
    PrimaryKeyConstraint,
    Sequence,
    Table,
    ThreadLocalMetaData,
    UniqueConstraint,
    DDL,
    BLANK_SCHEMA
)
#####结构化查询语言
from .sql import (
    alias,
    all_,
    and_,
    any_,
    asc,
    between,
    bindparam,
    case,
    cast,
    collate,
    column,
    delete,
    desc,
    distinct,
    except_,
    except_all,
    exists,
    extract,
    false,
    func,
    funcfilter,
    insert,
    intersect,
    intersect_all,
    join,
    lateral,
    literal,
    literal_column,
    modifier,
    not_,
    null,
    nullsfirst,
    nullslast,
    or_,
    outerjoin,
    outparam,
    over,
    select,
    subquery,
    table,
    tablesample,
    text,
    true,
    tuple_,
    type_coerce,
    union,
    union_all,
    update,
    within_group,
)

####字段类型
from .types import (
    ARRAY,
    BIGINT,
    BINARY,
    BLOB,
    BOOLEAN,
    BigInteger,
    Binary,
    Boolean,
    CHAR,
    CLOB,
    DATE,
    DATETIME,
    DECIMAL,
    Date,
    DateTime,
    Enum,
    FLOAT,
    Float,
    INT,
    INTEGER,
    Integer,
    Interval,
    JSON,
    LargeBinary,
    NCHAR,
    NVARCHAR,
    NUMERIC,
    Numeric,
    PickleType,
    REAL,
    SMALLINT,
    SmallInteger,
    String,
    TEXT,
    TIME,
    TIMESTAMP,
    Text,
    Time,
    TypeDecorator,
    Unicode,
    UnicodeText,
    VARBINARY,
    VARCHAR,
)

__version__ = '1.2.7'


def __go(lcls):
    global __all__

    from . import events
    from . import util as _sa_util

    ### 判断是否是模块
    import inspect as _inspect

    # sorted([i for i in range(5)])
    # sorted(i for i in range(5))
    # 可省略（）
    __all__ = sorted(name for name, obj in lcls.items()
                     if not (name.startswith('_') or _inspect.ismodule(obj)))

    _sa_util.dependencies.resolve_all("sqlalchemy")


__go(locals())


## 只导出变量或者函数名，像下面这样模块或者内置的属性,以及私有变量（比_开头的），将过滤掉
# ['__builtins__', '__cached__', '__doc__', '__file__', '__go', '__loader__', '__name__', '__package__', '__spec__']

