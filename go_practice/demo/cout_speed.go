package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	const distance = 56000000.0
	var hour float64 = 28.0 * 24.0
	fmt.Println(distance / hour)
	a := 0.1
	a += 0.2
	fmt.Println(a)
	fmt.Println(a == 0.3)
	c := 0.0
	arr := []float64{0.05, 0.20, 0.50} //声明数组
	rand.Seed(time.Now().Unix())
	for c < 20 {
		c += arr[rand.Intn(3)]
		fmt.Printf("%4.2f\n", c)
	}
}
