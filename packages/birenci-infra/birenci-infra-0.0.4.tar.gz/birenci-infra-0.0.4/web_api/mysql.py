from flask_sqlalchemy import SQLAlchemy


class MySQLAlchemy(SQLAlchemy):
    def apply_pool_defaults(self, app, options):
        super(MySQLAlchemy, self).apply_pool_defaults(app, options)
        options["pool_pre_ping"] = True
        options["pool_recycle"] = 60
        options["max_overflow"] = 100
        return options


mysql = MySQLAlchemy()
# Model = mysql.Model
metadata = mysql.metadata
