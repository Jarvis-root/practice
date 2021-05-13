package main

import (
	"fmt"
	"math/rand"
	"time"
)

// 值传递: 是指在调用函数时将实际参数复制一份传递到函数中，这样在函数中如果对参数进行修改，将不会影响到实际参数。
// 引用传递: 是指在调用函数时将实际参数的地址传递到函数中，那么在函数中对参数所进行的修改，将影响到实际参数。
// 默认情况下，Go 语言使用的是值传递，即在调用过程中不会影响到实际参数。

func Demo(x, y int) (add, mul int) { //多参数，多返回值。返回值可以写名字也可以只写类型。
	return x + y, x * y
}

func demo(x, y int) (add, mul int) { //函数名首字符小写，只能在包内部使用。首字符大写在其他包也可以用。
	return x + y, x * y
}

func Good(args ...interface{}) { //...表示参数数量是可以变的，args是一个空接口。组合到一起可以接受任意数量个类型的参数
}

type Mytype func() int //可以为函数声明类型

func closure(x int) Mytype { //闭包
	var k = 1
	return func() int { //匿名函数，go在函数里面不在声明带名字的函数
		return k + x
	}
}

// 函数是一等公民，可以赋值给变量，可以作为参数传递，可以当作返回值。通过函数里面创建匿名函数可以构成闭包
func main() {
	d := Demo //函数复制给变量
	fmt.Println(d(2, 3))

	f := closure(1) //闭包
	fmt.Println(f())
	fmt.Println(f())
	fmt.Println(f())

	rand.Seed(time.Now().UnixNano())
	arr := [...]int{1, 2, 3, 4, 5} //... 表示省略长度，编译器自动判断
	// f := func(i, j int) {
	// 	arr[i], arr[j] = arr[j], arr[i]
	// }
	var a, b = 1, 2
	fmt.Println(a, b)
	a, b = b, a // go支持这个，和py一样很好
	fmt.Println(a, b)
	rand.Shuffle(len(arr), func(i, j int) { //函数也可以作为参数传递
		arr[i], arr[j] = arr[j], arr[i]
	}) //匿名函数，go在函数里面不在声明带名字的函数
	fmt.Println(arr)

}
