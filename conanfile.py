import os

from conans import ConanFile, tools


class IodConan(ConanFile):
    name = "iod"
    version = "0.1"
    license = "MIT"
    author = "Matthieu Garrigues <matthieu.garrigues@gmail.com>"
    url = "https://github.com/BlueSolei/conan-iod"
    description = "Meta programming utilities for C++14"
    topics = ("c++", "c-plus-plus", "meta-programming",
              "serialization", "deserialization")
    no_copy_source = True
    scm = {
        "type": "git",
        "url": "https://github.com/matt-42/iod",
        "revision": "master"
    }
    # No settings/options are necessary, this is header only

    def package(self):
        self.copy("iod/*.*", "include")
