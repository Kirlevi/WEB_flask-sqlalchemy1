# from data.marsians import User, Jobs
from data.users import User, News
from data.db_session import global_init
from data.db_session import create_session


global_init("db/blogs.sqlite")


