#lang racket

(require "util.rkt")

(define (palindrome? n)
  (equal? (digits n) (reverse (digits n))))

; I cheated a little bit on this one, but mainly because I'm trying to learn Racket
; moreso than figure out the math of this problem a second time.
; Credits to http://blog.jverkamp.com/2012/11/07/project-euler-4/
(for*/fold ([best 0])
           ([x (in-range 100 1000)]
            [y (in-range 100 1000)]
            #:when (palindrome? (* x y)))
  (when (palindrome? (* x y)) (max best (* x y))))
