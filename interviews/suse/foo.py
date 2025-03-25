"""
// Given these flat, space-delimited files. Write a function that prints the ids of the rows where:
//   a) the ids match across the files and
//   b) the value is "foo" for that id in both files
//
// -------- file1.txt ------
// ID     VALUE
// 3x   foo
// a2                    bar
// 1a       foo
// f4             Foo
// ...
// N        baz
// ------------------------
//
// -------- file2.txt --------
// ID     VALUE
// 1a           xyz
// 3x         foo
// 2b     abc
// a2         bar
// f4        Foo
// adfhjgl     foo
// ...
// N        bing
// ------------------------
"""