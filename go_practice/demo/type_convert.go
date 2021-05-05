package main

import (
	"fmt"
	"strconv"
)

func main() {
	var a int = 13231
	fmt.Printf("type: %T\n", float64(a)) // 类型转换，和python有点像

	var b float64 = 13231.55
	fmt.Printf("type: %T, %v\n", int(b), int(b))

	// fmt.Println(math.MaxUint8)
	n := 65
	fmt.Println("string(n):", string(n)) // 这样转换是将整数转成对于的unicode字符（rune）
	s := fmt.Sprint(n)                   // 这样才是将数字转成字符
	fmt.Printf("%T, %v\n", s, s)

	ascii := strconv.Itoa(n)
	fmt.Printf("%T, %v\n", ascii, ascii) //strconv包用来转

	str := "666"
	i, err := strconv.Atoi(str) // 这个函数如果字符串有数字以外的字符会有异常
	if err != nil {             //go的异常不是抛出的，而是return的，一般是最后一个返回值。没有try catch
		fmt.Println(err)
	}
	fmt.Printf("%T, %v\n", i, i)
}
