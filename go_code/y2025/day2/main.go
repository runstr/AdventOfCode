package main

import (
	"os"
	"strconv"
	"strings"
)

func get_my_answer() {
	content, err := os.ReadFile("C:\\Users\\Rune\\AdventOfCode\\go_code\\y2025\\day2\\example.txt")
	if err != nil {
		panic(err)
	}
	input := strings.Split(string(content), ",")
	println(input)

	invalid_ids = []int
	for i := 0; i < len(input); i++ {
		temp := strings.Split(string(content), ",")
		first, _ := strconv.Atoi(temp[0])
		second, _ := strconv.Atoi(temp[1])
		for y := first; y <= second; y++ {
			number := string(y)
			test_sequence := ""
			for index := 0; index <= len(number)/2; index++ {
				test_sequence += string(number[0])
			}
		}

	}

	/*     invalid_ids = []
	       for sequence in sequences:
	           first, second = map(int, sequence.split("-"))
	           for num in range(first, second+1):
	               number = str(num)
	               test_sequence = ""
	               for index in range(0, len(number)//2+1):
	                   test_sequence += number[index]
	                   mult = len(number) // len(test_sequence)
	                   if  test_sequence * int(mult) == number and mult !=1:
	                       invalid_ids.append(int(number))
	                       break
	       return sum(invalid_ids) */
}
func main() {
	get_my_answer()
}
