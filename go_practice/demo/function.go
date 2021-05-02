package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())
	arr := [...]int{1, 2, 3, 4, 5}
	// f := func(i, j int) {
	// 	arr[i], arr[j] = arr[j], arr[i]
	// }
	var a, b = 1, 2
	fmt.Println(a, b)
	a, b = b, a // go支持这个，和py一样很好
	fmt.Println(a, b)
	rand.Shuffle(len(arr), func(i, j int) {
		arr[i], arr[j] = arr[j], arr[i]
	}) //匿名函数，go在函数里面不在声明带名字的函数
	fmt.Println(arr)

}
