mongo_engine = {
    "MONGODB_SETTINGS": {
        "db": "jenkins_result",
        "host": "10.50.20.3",
        "port": 27017,
        "connect": False,
    }
}


class Config:
    mongo_engine = mongo_engine
