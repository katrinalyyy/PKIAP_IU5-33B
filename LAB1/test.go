package main

import (
	"errors"
	"strconv"
	"strings"
)

func IsDigit(elem string) bool {
	for _, letter := range "0123456789." {
		if elem == string(letter) {
			return true
		}
	}
	return false
}

// Проверка на допустимые символы
func isValidExpression(s string) bool {
	for _, char := range s {
		if !strings.ContainsRune("0123456789.+-*/() ", char) {
			return false
		}
	}
	return true
}

func Calc(s string) (float64, error) {
	s = strings.ReplaceAll(s, " ", "")

	// Проверка на недопустимые символы
	if !isValidExpression(s) {
		return 0, errors.New("некорректный ввод: недопустимые символы")
	}

	// Проверка на некорректные символы в конце строки
	if len(s) == 0 || strings.ContainsAny(s[len(s)-1:], "+-*/") {
		return 0, errors.New("некорректный ввод: строка не должна заканчиваться на оператор")
	}

	var mix_s []interface{}
	var current_num string

	// Разбиваем строку на числа и операторы
	for i := 0; i < len(s); i++ {
		if IsDigit(string(s[i])) {
			current_num += string(s[i])
		} else {
			if current_num != "" {
				if len(current_num) > 1 && current_num[0] == '0' && current_num[1] != '.' {
					return 0, errors.New("число не может начинаться с нуля: " + current_num)
				}
				num, err := strconv.ParseFloat(current_num, 64)
				if err != nil {
					return 0, errors.New("ошибка преобразования числа: " + err.Error())
				}
				mix_s = append(mix_s, num)
				current_num = ""
			}
			if i > 0 && strings.ContainsAny(string(s[i]), "+-*/") && strings.ContainsAny(string(s[i-1]), "+-*/") {
				return 0, errors.New("некорректный ввод: последовательные операторы")
			}
			mix_s = append(mix_s, string(s[i]))
		}
	}

	if current_num != "" {
		if len(current_num) > 1 && current_num[0] == '0' && current_num[1] != '.' {
			return 0, errors.New("число не может начинаться с нуля: " + current_num)
		}
		num, err := strconv.ParseFloat(current_num, 64)
		if err != nil {
			return 0, errors.New("ошибка преобразования числа: " + err.Error())
		}
		mix_s = append(mix_s, num)
	}

	stek1 := make([]float64, 0)
	stek2 := make([]string, 0)

	for i := 0; i < len(mix_s); i++ {
		if num, ok := mix_s[i].(float64); ok {
			stek1 = append(stek1, num)
		} else if mix_s[i] == "(" {
			stek2 = append(stek2, mix_s[i].(string))
		} else if mix_s[i] == ")" {
			for len(stek2) > 0 && stek2[len(stek2)-1] != "(" {
				op := stek2[len(stek2)-1]
				stek2 = stek2[:len(stek2)-1]
				b := stek1[len(stek1)-1]
				stek1 = stek1[:len(stek1)-1]
				a := stek1[len(stek1)-1]
				stek1 = stek1[:len(stek1)-1]
				if op == "+" {
					stek1 = append(stek1, a+b)
				} else if op == "-" {
					stek1 = append(stek1, a-b)
				} else if op == "*" {
					stek1 = append(stek1, a*b)
				} else if op == "/" {
					if b == 0 {
						return 0, errors.New("деление на ноль")
					}
					stek1 = append(stek1, a/b)
				}
			}
			stek2 = stek2[:len(stek2)-1]
		} else {
			for len(stek2) > 0 && (stek2[len(stek2)-1] == "*" || stek2[len(stek2)-1] == "/" || (stek2[len(stek2)-1] == "+" || stek2[len(stek2)-1] == "-") && (mix_s[i] == "+" || mix_s[i] == "-")) {
				op := stek2[len(stek2)-1]
				stek2 = stek2[:len(stek2)-1]
				b := stek1[len(stek1)-1]
				stek1 = stek1[:len(stek1)-1]
				a := stek1[len(stek1)-1]
				stek1 = stek1[:len(stek1)-1]
				if op == "+" {
					stek1 = append(stek1, a+b)
				} else if op == "-" {
					stek1 = append(stek1, a-b)
				} else if op == "*" {
					stek1 = append(stek1, a*b)
				} else if op == "/" {
					if b == 0 {
						return 0, errors.New("деление на ноль")
					}
					stek1 = append(stek1, a/b)
				}
			}
			stek2 = append(stek2, mix_s[i].(string))
		}
	}

	for len(stek2) > 0 {
		op := stek2[len(stek2)-1]
		stek2 = stek2[:len(stek2)-1]
		b := stek1[len(stek1)-1]
		stek1 = stek1[:len(stek1)-1]
		a := stek1[len(stek1)-1]
		stek1 = stek1[:len(stek1)-1]
		if op == "+" {
			stek1 = append(stek1, a+b)
		} else if op == "-" {
			stek1 = append(stek1, a-b)
		} else if op == "*" {
			stek1 = append(stek1, a*b)
		} else if op == "/" {
			if b == 0 {
				return 0, errors.New("деление на ноль")
			}
			stek1 = append(stek1, a/b)
		}
	}
	return stek1[0], nil
}
