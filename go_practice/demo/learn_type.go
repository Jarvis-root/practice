package main

import (
	"fmt"
	"math"
	"math/big"
)

func Integer() {
	year := 2021
	fmt.Printf("year 的类型是：%T\n", year)

	a := "aaaa"
	fmt.Printf("a 的类型是：%T\n", a)

	b := true
	fmt.Printf("b 的类型是：%T\n", b)

	c := .2
	fmt.Printf("c 的类型是：%T\n", c)

	d := 'd' // 单引号表示字符，在go里面叫rune。rune是int32的别名
	fmt.Printf("d 的类型是：%T, 值是%v\n", d, d)

	var red uint8 = 255 // 整数环绕，uint8：0-255，超过范围会环绕
	red++
	fmt.Println(red)

	var n int8 = 127 // 整数环绕，int8：-128-127，超过范围会环绕
	n++
	fmt.Println(n)

	fmt.Println("最大的int64：", math.MaxInt64)
	fmt.Println("1<<63-1：", 1<<63-1)

	fmt.Printf("3e11的类型是：%T\n", 3e11) //指数类型默认是float64

	fmt.Println(big.NewInt(3e11))      //big包可以表示大数和计算
	var bigInt *big.Int = new(big.Int) //big.Int，另外一种使用方法
	// bigInt := new(big.Int)
	bigInt.SetString("66666666666666666666", 10)
	fmt.Println(bigInt) //big包可以表示大数和计算

}
func main() {
	Integer()
}
