#lang racket

(require "util.rkt")

(sum (filter (lambda (x) (or (= 0 (modulo x 3)) (= 0 (modulo x 5)))) (range 1 1000)))
