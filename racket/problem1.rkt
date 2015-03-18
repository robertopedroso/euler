#lang racket
(define (sum lst)
  (cond
    [(empty? lst) 0]
    [else (+ (first lst) (sum (rest lst)))]))
(sum (filter (lambda (x) (or (= 0 (modulo x 3)) (= 0 (modulo x 5)))) (range 1 1000)))