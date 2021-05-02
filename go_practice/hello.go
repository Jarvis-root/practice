package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	// fmt.Println("hello, go")

	fmt.Printf("9 * 9999.02 = %v \n", 9*9989.02)

	// var a, b = 1, 2
	// fmt.Println(a, b)
	// var (
	// 	c = 3
	// 	d = 4
	// )
	// println(c, d) // 全局的println
	// /*
	// 	lalalalallalalallala
	// */
	// const e, f = 1, 2
	// // a = 3  编译报错
	// println(a, b)

	var t = time.Now().Unix()
	println(t)
	rand.Seed(t)
	println(rand.Intn(10))
}
