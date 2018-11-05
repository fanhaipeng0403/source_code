##sqlalchemy 分为两个技术模块
#####################################################################################################

# sql expression language  这些构造被建模为尽可能接近底层数据库的构造
# ORM  基于sql expression language 构建的高级和抽象模式

# 区别
# ORM与构建ORM的SQLAlchemy表达式语言形成对比。
# 在SQL表达式语言教程中引入的SQL表达式语言提出了一种直接表示关系数据库的原始结构而中立的系统，
# 而ORM提供了一种高级和抽象的使用模式，它本身就是应用的一个例子。


# database-------------->sql expression language-------> ORM

#####################################################################################################


# CORE文档
# https://docs.sqlalchemy.org/en/latest/core/index.html

# SQL表达式语言教程

# 版本检查
# 连
# 定义和创建表
# 插入表达式
# 执行
# 执行多个语句
# 选择
# 运营商
# 连词
# 使用文本SQL
# 使用别名
# 使用连接
# 其他一切
# 插入，更新和删除
# 进一步参考


# SQL语句和表达式API

# 列元素和表达式
# 可选择项，表，FROM对象
# 插入，更新，删除
# SQL和通用函数
# 自定义SQL构造和编译扩展
# Expression Serializer Extension

# 模式定义语言

# 使用MetaData描述数据库
# 反映数据库对象
# 列插入/更新默认值
# 定义约束和索引
# 自定义DDL

# 列和数据类型

# 列和数据类型
# 自定义类型
# 基本类型API

# 引擎和连接使用

# 引擎配置
# 使用引擎和连接
# 连接池
# 核心事件

# 核心API基础知识

# 活动
# 运行时检查API
# 不推荐使用的事件接口
# 核心例外
# 核心内部

# ORM文档
# https://docs.sqlalchemy.org/en/latest/orm/index.html
#
# 对象关系教程

# 版本检查
# 连
# 声明映射
# 创建架构
# 创建映射类的实例
# 创建会话
# 添加和更新对象
# 滚回来
# 查询
# 建立关系
# 使用相关对象
# 查询加入
# 渴望加载
# 删除
# 建立多对多的关系
# 进一步参考

# 映射器配置

# 映射的类型
# 映射列和表达式
# 映射类继承层次结构
# 非传统映射
# 配置版本计数器
# 类映射API

# 关系配置

# 基本关系模式
# 邻接列表关系
# 将关系与Backref联系起来
# 配置关系如何连接
# 集合配置和技术
# 特殊关系持久性模式
# 关系API
# 加载对象
# 加载列
# 关系加载技术
# 加载继承层次结构
# 构造函数和对象初始化
# 查询API

# 使用会话

# 会话基础
# 国家管理
# 瀑布
# 交易和连接管理
# 额外的持久性技术
# 上下文/线程本地会话
# 使用事件跟踪对象和会话更改
# 会话API

# 事件和内部

# ORM活动
# ORM内部
# ORM例外
# 不推荐使用的ORM事件接口

# ORM扩展

# 关联代理
# 自动地图
# 烤查询
# 陈述
# 变异追踪
# 订购清单
# 水平分片
# 混合属性
# 可转位
# 替代级仪表

# ORM示例

# 映射食谱
# 继承映射食谱
# 特殊API
# 扩展ORM

# dialect 方言 dialect，是数据库类型，大概包括：sqlite, mysql, postgresql, oracle等

##### 数据库引擎，处理连接等
from .engine import create_engine, engine_from_config
###  检查监测功能，它在Core和ORM中提供有关各种SQLAlchemy对象的运行时信息。
from .inspection import inspect
#### 表的结构 ˈskiːmə,
#### 索引，约束, 默认值，DDL，sequence
from .schema import (

    # 表级和列级约束，程序和服务器端约束

    # 约束#
    ######################################################################################################################
    Constraint,
    PrimaryKeyConstraint,
    UniqueConstraint,

    # __table_args__ = (UniqueConstraint('currency_type', 'orig_id', name='ix_uniq_currency_type_and_orig_id'),
    #                   Index('ix_og_account_and_user_id_updated', 'og_account', 'user_id_updated'),
    #                   Index('ix_og_account_and_user_id', 'user_id', 'og_account'))
    CheckConstraint,
    ForeignKeyConstraint,
    # A table- or column-level

    # class Foo(Base):
    #     __tablename__ = 'foo'
    #     id = Column(Integer, primary_key=True)
    #     bar = Column(Integer)
    #     __table_args__ = (
    #         CheckConstraint(bar >= 0, name='check_bar_positive'),
    #         {})

    # per-column CHECK constraint
    # Column('col1', Integer, CheckConstraint('col1>5')),
    # Column('col2', Integer),
    # Column('col3', Integer),
    # CheckConstraint('col2 > col3 + 5', name='check1')

    # id = Column(Integer, primary_key=True, autoincrement=True)

    # 默认值#
    #######################################################################################################################
    ColumnDefault,
    DefaultClause,
    # 弃用
    PassiveDefault,

    # sever_default(服务端设置）
    # DefaultClause

    # Column('foo', Integer, server_default="50")等效于 Column('foo', Integer, DefaultClause("50"))

    # default
    # ColumnDefault
    # Column('foo', Integer, default=50)  等效于  Column('foo', Integer, ColumnDefault(50))

    #######################################################################################################################

    DDL,
    # 专门用于写给event监听事件时，使用DDL原生语法
    # event.listen(tbl, 'before_create', DDL('DROP TRIGGER users_trigger'))
    # https://stackoverflow.com/questions/12039046/in-sqlalchemy-how-do-i-define-an-event-to-fire-ddl-using-declarative-syntax
    #######################################################################################################################
    BLANK_SCHEMA,
    FetchedValue,
    ForeignKey,
    #######################################################################################################################

    # https://n3xtchen.github.io/n3xtchen/postgresql/2015/04/10/postgresql-sequence
    Sequence,

    # some_table = Table(
    # 'some_table', metadata,
    # Column('id', Integer, Sequence('some_table_seq'),
    #        primary_key=True) )

    # 'some_table_seq' 就是的sequence规则，
    # 比如
    # [2,4,6,8,10,2,4,6,8,10],差值2，最大10，循环？？？？

    # Sequence是数据库系统按照一定规则自动增加的数字序列。这个序列一般作为代理主键（因为不会重复），没有其他任何意义。
    # Sequence是数据库系统的特性，有的数据库有Sequence，有的没有。比如Oracle、DB2、PostgreSQL数据库有Sequence，MySQL、SQL Server、Sybase等数据库没有Sequence。
    # 根据我个人理解，Sequence是数据中一个特殊存放等差数列的表，该表受数据库系统控制，任何时候数据库系统都可以根据当前记录数大小加上步长来获取 到该表下一条记录应该是多少，这个表没有实际意义，常常用来做主键用

    # 在MySQL中，序列最简单的用法就是将一列定义为 AUTO_INCREMENT ，然后让 MySQL 来处理剩下的任务。
    # PostgreSQL 中的序列是一个数据库对象，本质上是一个自增器。因此，序列在其他同类型数据库软件中以 autoiNcrment 值的形式存在。

    #######################################################################################################################

    Index,

    # __table_args__ = (UniqueConstraint('currency_type', 'orig_id', name='ix_uniq_currency_type_and_orig_id'),
    #                   Index('ix_og_account_and_user_id_updated', 'og_account', 'user_id_updated'),
    #                   Index('ix_og_account_and_user_id', 'user_id', 'og_account'))
    MetaData,

    # 第一种CORE,SQL Expression Language

    # from sqlalchemy import create_engine, MetaData,\
    #         Table, Column, Integer, String, ForeignKey
    #
    # engine = create_engine('mysql+mysqldb://root:******@localhost/sa_test', echo=True)

    # metadata = MetaData(engine)  若不绑定的，后面调用metadata.create_all(engine)

    # user_table = Table('user', metadata,
    #         Column('id', Integer, primary_key=True),
    #         Column('name', String(50)),
    #         Column('fullname', String(100))
    #         )
    #
    # address_table = Table('address', metadata,
    #         Column('id', Integer, primary_key=True),
    #         Column('user_id', None, ForeignKey('user.id')),
    #         Column('email', String(128), nullable=False)
    #         )
    #
    # metadata.create_all()

    # with engine.connect() as connect:
    # result= conn.execute( select([users.c.name, users.c.fullname])

    # 第二种ORM

    # engine = create_engine('sqlite:///./cnblogblog.db', echo=True)
    # Base = declarative_base()
    # DBSession = sessionmaker(bind=engine)
    #
    #
    # class User(Base):
    #     """Users table"""
    # __tablename__ = 'users'
    # __table_args__ = {'sqlite_autoincrement': True}
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # name = Column(String(32), nullable=False)
    # age = Column(Integer, default=0)
    # password = Column(String(64), unique=True)

    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine)
    Table,
    ThreadLocalMetaData,

    # 第三种：
    # 混合

)
#####结构化查询语言
from .sql import (
    ###用在 result= conn.execute( select([users.c.name, users.c.fullname])这样的sql expression language中
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
# http://www.codexiu.cn/python/SQLAlchemy%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B/532/
##### 这里只介绍 sqlalchemy.types.* 中的类型, SQL 标准类型方面, 是写什么最后生成的 DDL 语句就是什么, 比如 BIGINT, BLOG 这些, 但是这些类型并不一定在所有数据库中都有支持.  除此而外, SQLAlchemy  也支持一些特定数据库的特定类型, 这些需要从具体的 dialects 实现里导入.

# 有三种概念

# 1.兼容多个后端的数据库，并且和Python内置数据结构关联 ,如String,特点，首字母大写，其余小写
# 2.写什么 create table就是什么，如VARCHAR,特点，全大写
# 3.特定dialects数据库的特定类型
from .types import (

    # 第一种 兼容多个后端的数据库，并且和Python内置数据结构关联 ,如String,特点，首字母大写，其余小写
    #########################################################################################################################################
    # 整型
    SmallInteger,
    BigInteger,
    Integer,
    # 浮点型
    Float,  # 浮点小数.
    # 精确的浮点型
    # 定点小数, Python 中表现为 Decimal .
    Numeric,
    # 字符串
    # https://www.cnblogs.com/zejin2008/p/6606120.html
    # https://blog.csdn.net/Gane_Cheng/article/details/52316408
    # 字符串类型, Python 中表现为 Unicode , 数据库表现为 VARCHAR , 通常都需要指定长度.
    String,
    # 文档
    Text,
    # 长文本类型, Python 表现为 Unicode , 数据库表现为 TEXT .
    Time,
    # 日期
    DateTime,
    # Python中的datetime.date	日期
    Date,

    # 布尔
    Boolean,
    PickleType,
    # Python 对象的序列化类型.
    Enum,
    # Enum (*enums, **kw)
    # 枚举类型, 根据数据库支持情况, SQLAlchemy 会使用原生支持或者使用 VARCHAR 类型附加约束的方式实现. 原生支持中涉及新类型创建, 细节在实例化时控制.
    LargeBinary,
    # 字节数据. 根据数据库实现, 在实例化时可能需要指定大小.
    Binary,
    # 字节数据. 根据数据库实现, 在实例化时可能需要指定大小.

    Unicode,
    UnicodeText,

    # 第二种写什么 create table就是什么，如VARCHAR,特点，全大写
    #########################################################################################################################################
    SMALLINT,  # 2个字节
    INTEGER,
    INT,  # 4个字节
    BIGINT,  # 存储大小为 8 个字节

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # binary 与 varbinary 类型和char与varchar类型是相似的，只是他们存储的是二进制数据，也就是说他们是包含字节流而不是字符流，他们有二进制字符的集合和顺序，他们的对比，排序是基于字节的数值进行的
    # binary与varbinary的最大长度和char与varchar是一样的，只不过他们是定义字节长度，而char和varchar对应的是字符长度
    BINARY,
    VARBINARY,
    CHAR,  # 不可变。用于长度不怎么变或者相近的
    VARCHAR,  # 可变长度的
    FLOAT,
    DATE,
    DATETIME,
    NUMERIC,
    DECIMAL,
    TIME,
    TIMESTAMP,
    TEXT,

    #########################################################################################################################################
    ARRAY,
    BLOB,
    BOOLEAN,
    CLOB,
    Interval,
    JSON,
    NCHAR,
    NVARCHAR,
    REAL,
    TypeDecorator,

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
