# Conan Package for Pistache

## What is this?

This is my attempt to learn about making an unstable [conan](https://conan.io) package for [pistache](http://pistache.io/), versioned on commit.

I used the sources found in the [conan-community/conan-pistache](https://github.com/conan-community/conan-pistache) repo as a useful starting point so the initial commit contains large amounts of that work verbatim.

## Basic setup

> $ `conan install pistache/c5ff6f9@serialprimate/unstable`

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt* with the configuration like so for example:

```ini
[requires]
pistache/c5ff6f9@serialprimate/unstable

[options]
pistache:shared=True

[generators]
cmake
```

Complete the installation of requirements for your project running:

> $ `conan install .`

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.

## Notes

1. It's mostly clean only due to the fact the example is *derived from another repo*.
2. Given that the package is "commit versioned", I'm not too sure about how to maintain versions and create new ones. Some examples online maintain git branches named with the package source version.
3. It's not perfect. All hints and/or tips are welcome.

## No Warranty

There is no warranty of fitness for a particular purpose or merchantability.
