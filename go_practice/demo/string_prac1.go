package main

import (
	"fmt"
	"unicode/utf8"
)

func main() {
	s := "我在学习啦啦啦"
	fmt.Println("bytes:", len(s)) // len函数返回的是字符串的字节数，而不是字符串的长度

	fmt.Println("字符数：", utf8.RuneCountInString(s)) // 这样才能数字符个数

	for index, char := range s { //按字符占用的字节来遍历的，index不是按1递增的，因为中文占用的字节更多
		// fmt.Println(index, char)
		fmt.Printf("%v %c\n", index, char)
	}
	arr := []string{"aaaa", "bbb"}
	for index, str := range arr { //range是关键字，有点像py的enumerate函数
		// fmt.Println(index, char)
		fmt.Printf("%v %v\n", index, str)
	}
}
