#lang racket

(require "util.rkt")

(define (gpf n)
  (define (rec-gpf i n)
    (cond [(>= (expt i 2) n) n]
          [(divides? n i) (rec-gpf i (/ n i))]
          [else (rec-gpf (+ i 1) n)]))
  (rec-gpf 2 n))