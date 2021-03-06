(defun recaman (lim)
     (let ((res '(0)))
       (dotimes (x lim res)
	 (let* ((cur (car res))
		(opt1 (- cur (+ x 1)))
		(opt2 (+ cur (+ x 1))))
	   (if (or (< opt1 0) (member opt1 res))
	       (setq res (cons opt2 res))
	     (setq res (cons opt1 res)))
	   ))
       (car res)))
