(DEFUN FACTORIAL (N)
  (IF (= N 0)
      1
      (* N (FACTORIAL (- N 1)))))

(PRINT (FACTORIAL 5))
