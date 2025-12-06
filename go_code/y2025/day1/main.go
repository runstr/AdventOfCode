package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func convert_line(input string) (string, int) {
	direction := input[:1]
	string_int := input[1:]
	integer, err := strconv.Atoi(string_int)
	if err != nil {
		panic(err)
	}
	return direction, integer

}
func main() {
	var content []byte
	var err error
	content, err = os.ReadFile("C:\\Users\\Rune\\AdventOfCode\\go_code\\y2025\\day1\\input.txt")
	var string_content string
	string_content = string(content)
	var split_string []string
	split_string = strings.Split(string_content, "\r\n")
	if err != nil {
		fmt.Println("Error reading file:", err)
		return
	}
	clock_value := 50
	zero_entries := 0
	zero_passings := 0
	for i := 0; i < len(split_string); i++ {
		direction, steps := convert_line(split_string[i])
		clock_value, zero_passings = check_movement(clock_value, zero_passings, steps, direction)
		if clock_value == 0 {
			zero_entries += 1
		}
		println(direction, steps, "-->", clock_value, zero_passings)
	}
	fmt.Println("Answer 1: ", zero_entries)
	fmt.Println("Answer 2: ", zero_passings)

}

func check_movement(dial int, zero_passings int, steps int, letter string) (int, int) {
	zero_passings += steps / 100
	steps = steps % 100
	if letter == "R" {
		dial += steps
		if dial >= 100 {
			zero_passings += 1
		}
	} else {
		if dial == 0 {
			zero_passings -= 1
		}
		dial -= steps
		if dial <= 0 {
			zero_passings += 1
			dial = 100 + dial
		}
	}
	dial = dial % 100
	return dial, zero_passings
}
