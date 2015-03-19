#lang racket

(provide sum)
(provide define-memoized)
(provide divides?)

; sum a list of numbers
(define (sum lst)
  (cond
    [(empty? lst) 0]
    [else (+ (first lst) (sum (rest lst)))]))

; memoized version of define
; from: http://blog.jverkamp.com/2012/10/20/memoization-in-racket/
(define-syntax define-memoized
  (syntax-rules ()
    [(_ (f args ...) bodies ...)
     (define f
       (let ([results (make-hash)])
         (lambda (args ...)
           ((lambda vals
              (when (not (hash-has-key? results vals))
                (hash-set! results vals (begin bodies ...)))
              (hash-ref results vals))
            args ...))))]))

; returns whether a is divisible by b
(define (divides? a b)
  (zero? (remainder a b)))
