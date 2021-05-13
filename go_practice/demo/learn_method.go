package main

import (
	"fmt"
)

// 方法：与类型相关联的函数。go没有class和对象，但是有方法
// 声明新的类型：使用type关键字

type name string // 声明name类型
type age int     // 声明age类型

func (n name) IsAdult(a age) name { //与name类型相关联的方法，返回值是name类型。方法只能关联一个类型
	if a >= 18 {
		return name(n + " is an adult") //这个不是递归，是创建一个name
	}
	return name(n + " is not an adult")
}

func main() {
	var a name = "jack"
	var i age = 19
	fmt.Println(a.IsAdult(i)) //调用方法必须使用对应类型的变量
}
