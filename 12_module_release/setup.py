from distutils.core import setup

setup(name="message",
      version="1.0",
      description="发送和接受消息模块",
      long_description="完整的发送和接受消息模块",
      author="DeveloperLY",
      author_email="coderyliu@gmail.com",
      url="http://www.developerly.net",
      py_modules=[
          "message.send_message",
          "message.receive_message"
      ])

"""
$ python3 setup.py build
$ python3 setup.py sdist

$ python3 setup.py install

$ cd /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages
$ ls -l | grep message
$ rm -r message*
"""