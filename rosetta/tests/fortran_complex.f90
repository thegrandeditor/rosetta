PROGRAM TEST_FORTRAN
  IMPLICIT NONE
  INTEGER :: I, J
  REAL :: A(10)
  COMMON /BLK/ I, J
  
  PRINT *, "Starting test"
  DO I = 1, 10
    A(I) = I * 1.5
  END DO
  
  IF (A(5) > 5.0) THEN
    WRITE(*,*) "A(5) is large", A(5)
  ELSE
    WRITE(*,*) "A(5) is small", A(5)
  END IF
  
  CALL SUB1(J)
  PRINT *, "J is", J
  
  10 FORMAT("Result: ", F10.2)
END PROGRAM TEST_FORTRAN

SUBROUTINE SUB1(X)
  INTEGER :: X
  X = 42
  RETURN
END SUBROUTINE SUB1
