mongo_engine = {
    "MONGODB_SETTINGS": {
        "db": "jenkins_result",
        "host": "localhost",
        "port": 27017,
        "connect": False,
    }
}


class HRServer:
    host = "hr.birentech.com"
    port = "80"
    baseUrl = "https://hr.birentech.com/BirenApi"
    headers = {"ExternalServiceKey": "D83903B7-F90A-18Q1-E7F3-2E80F95056F9"}


class Config:
    mongo_engine = mongo_engine
    hrServer = HRServer
