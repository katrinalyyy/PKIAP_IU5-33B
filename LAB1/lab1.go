package main

import (
	"fmt"
	"math"
)

func check(a, b, c float64) bool {
	if a == 0 && b == 0 && c == 0 {
		fmt.Println("x принадлежит R")
		return true
	} else if a == 0 && c == 0 {
		fmt.Println("x = 0")
		return true
	} else if a == 0 && b == 0 {
		fmt.Println("Нет действительных корней")
		return true
	} else if a == 0 && b != 0 && c != 0 {
		t := -c / b
		if t > 0 {
			x1 := math.Sqrt(t)
			x2 := -math.Sqrt(t)
			fmt.Printf("Корни уравнения: %g, %g\n", x1, x2)
		} else if t == 0 {
			fmt.Println("x = 0")
		} else {
			fmt.Println("Нет действительных корней")
		}
		return true
	}
	return false
}

func discriminant(a, b, c float64) float64 {
	return b*b - 4*a*c
}

func solveQuadratic(a, b, c float64) []float64 {
	D := discriminant(a, b, c)
	if D > 0 {
		t1 := (-b + math.Sqrt(D)) / (2 * a)
		t2 := (-b - math.Sqrt(D)) / (2 * a)
		return []float64{t1, t2}
	} else if D == 0 {
		t := -b / (2 * a)
		return []float64{t}
	}
	return nil
}

func returnX(a, b, c float64) []float64 {
	tRes := solveQuadratic(a, b, c)
	var res []float64

	for _, t := range tRes {
		if t > 0 {
			res = append(res, math.Sqrt(t), -math.Sqrt(t))
		} else if t == 0 {
			res = append(res, 0)
		}
	}
	return res
}

func checkABC(prompt string) float64 {
	var value float64
	for {
		fmt.Print(prompt)
		_, err := fmt.Scan(&value)
		if err == nil {
			break
		} else {
			fmt.Println("Некорректный ввод. Введите число.")
		}
	}
	return value
}

func main() {
	a := checkABC("Введите коэффициент A: ")
	b := checkABC("Введите коэффициент B: ")
	c := checkABC("Введите коэффициент C: ")

	if check(a, b, c) {
		return
	}

	xRes := returnX(a, b, c)
	if len(xRes) > 0 {
		fmt.Print("Корни уравнения:  ")
		for _, x := range xRes {
			fmt.Printf("%g ", x)
		}
		fmt.Println()
	} else {
		fmt.Println("Нет действительных корней")
	}
}
