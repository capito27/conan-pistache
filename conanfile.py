from os import path
from conans import ConanFile, CMake, tools


class PistacheConan(ConanFile):
    name = "pistache"
    version = "c5ff6f9"
    license = "Apache License 2.0"
    url = "git@gitlab.com:serialprimate/conan-pistache.git"
    description = "A high-performance REST Toolkit written in C++"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=False"
    generators = "cmake"

    @property
    def src_folder(self):
        return "{}-{}".format(self.name, self.version)

    def source(self):
        git = tools.Git(folder=self.src_folder)
        git.clone("https://github.com/oktal/pistache.git", "master")
        git.checkout(element=self.version)
        tools.replace_in_file(path.join(self.src_folder, 'CMakeLists.txt'), 'project (pistache)',
            """project (pistache)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PISTACHE_BUILD_TESTS"] = False
        cmake.definitions["PISTACHE_BUILD_EXAMPLES"] = False
        cmake.configure(source_folder=self.src_folder)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["pistache", "atomic", ]
        self.cpp_info.cppflags = ["-pthread", ]


