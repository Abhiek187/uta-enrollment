import os

class Config(object):
	SECRET_KEY = os.environ.get("SECRET_KEY") or b'\xe4&\xf6q&\x0e\xb5\xef\xe26\xf8\xdd\x9a&m~'

	MONGODB_SETTINGS = { "db": "UTA_Enrollment" }
