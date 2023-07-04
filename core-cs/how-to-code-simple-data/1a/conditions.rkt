(module conditions racket
	(define WIDTH 100)
	(define HEIGHT 100)

	(> WIDTH HEIGHT)
	(string=? "foo" "foo")

	(if (< 100 1000)
		"100 is less than 1000"
		"100 is more than 1000"
		)
)
