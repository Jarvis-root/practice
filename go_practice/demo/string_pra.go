package main

import (
	"fmt"
	"math/rand"
	"strings"
	"time"
)

var global = "这是全局变量" //可以在包全局申明变量

func get_rand_char() string {
	rand.Seed(time.Now().Unix())
	var arr [5]string
	arr[0] = "a"
	arr[1] = "b"
	arr[2] = "c"
	arr[3] = "d"
	arr[4] = "e"
	// fmt.Println(arr)
	return arr[rand.Intn(5)]
}
func s() string {
	var str string = "lalalalalla"
	fmt.Println(strings.Contains(str, "a"))
	return str
}

func loop() {
	// i := 5 短声明（python3.8的赋值表达式）
	for i := 5; i > 0; i-- { //go没有while循环
		fmt.Println(i)
	}
	i := 5
	for i > 0 { //也可以这样写
		fmt.Println(i)
		i--
	}
}

func main() {
	fmt.Println(global)
	s()
	if !true {
		var a = 1
		fmt.Println(a)
	} else if true {
		var a = 2
		fmt.Println(a)
	}
	// 这里也用了短声明，可以少写一句代码
	switch s := get_rand_char(); s {
	case "a":
		fmt.Println("matched1")
	case "b":
		fmt.Println("matched2")
		fallthrough //这个用来执行下一个case的body部分（不匹配也会执行）
	case "c":
		fmt.Println("matched3")
	}
	// loop()
}
