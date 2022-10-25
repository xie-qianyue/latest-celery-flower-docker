import os

USERNAME = os.getenv('USERNAME', 'admin')
PASSWORD = os.getenv('PASSWORD', 'qwer;1234')

port = int(os.getenv('FLOWER_PORT', '5555'))
max_tasks = int(os.getenv('FLOWER_MAX_TASKS', '300000'))
basic_auth = [os.getenv('FLOWER_BASIC_AUTH', '%s:%s'% (USERNAME, PASSWORD))]
persistent=True
purge_offline_workers=3600
