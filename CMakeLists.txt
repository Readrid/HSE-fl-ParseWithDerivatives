project(MatchRegexp)
cmake_minimum_required(VERSION 3.2)

add_compile_options(-std=c++17)

find_package(GTest REQUIRED)

add_executable(
        Regexp
        src/Regexp.cpp
        src/main.cpp
        include/Regexp.h
)

target_include_directories(
        Regexp
        PRIVATE
        ${GTEST_INCLUDE_DIRS}
)

target_link_libraries(
        Regexp
        GTest::GTest
)

set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})

target_compile_options(Regexp PRIVATE -Werror -Wall -Wextra)
include_directories(include/)