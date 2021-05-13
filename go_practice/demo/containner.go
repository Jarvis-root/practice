package main

import (
	"fmt"
)

func array() {
	var arr [2]int
	arr[0] = 1
	arr[1] = 2
	fmt.Println(arr)

	arr1 := [...]int{1, 2, 3, 4, 5} //声明并初始化，...可以自动判断长度
	fmt.Println(arr1)

	arr3 := [3][2]int{{}, {}, {}} //二维数组
	fmt.Println(arr3)

	// 遍历：
	i := len(arr)
	for i > 0 { //倒序遍历
		i--
		fmt.Println(arr[i])
	}
	for i := 0; i < len(arr); i++ {
		fmt.Println(arr[i])
	}
	for _, num := range arr { //不想使用的值和py一样，用下划线表示
		fmt.Println(num)
	}
	for i := range arr { // 这样的话，i就是直接是索引
		fmt.Println(arr[i])
	}

	var arr2 [2]int = arr // 赋值给新的变量和传给函数都会进行拷贝
	arr2[0] = 666
	fmt.Println(arr, arr2)

}

func slice() {
	arr1 := [...]int{1, 2, 3, 4, 5}
	//数组传给函数拷贝会影响效率，所以可以用切片后传递
	slice := arr1[0:3]        // go的切片不能是附属负数。字符串也可以切换，但是切的是字节数
	fmt.Printf("%T\n", slice) //[]int 表示slice，方括号中间啥也没有就是slice
	slice[0] = 777            //slice被改变原数组也会变
	fmt.Println(slice)
	fmt.Println(arr1)

	slice1 := []string{"a", "da"} //slice也可以直接创建，注意与数组的区别是中括号中间是空的
	fmt.Printf("%T\n", slice1)

	var slice2 = make([]int, 3, 5)               // 切片还可以通过make创建（make还可以创建map，cha），3是slice的长度（当前的元素个数），5是容量（最多可以容纳的元素数）
	slice2 = append(slice2, 6, 6, 6, 6, 6, 6, 6) //通过append追加元素，可以同时追加多个
	fmt.Printf("len=%d cap=%d slice2=%v\n", len(slice2), cap(slice2), slice2)

	slice3 := make([]int, len(slice2), len(slice2)*2)
	var count int = copy(slice3, slice2) //拷贝slice2的数据到slice3
	fmt.Println(count)
	fmt.Printf("len=%d cap=%d slice3=%v\n", len(slice3), cap(slice3), slice3)
}

func main() {
	array()
	fmt.Println("--------------------------------")
	slice()
}
